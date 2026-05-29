# ============================================
#   Student Grade Calculator
#   Author: Niyati Shah
#   B.Tech CSE, Indus University
# ============================================

def get_grade(percentage):
    """Return letter grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def get_gpa(percentage):
    """Return GPA (0-10 scale) based on percentage."""
    if percentage >= 90:
        return 10.0
    elif percentage >= 80:
        return 9.0
    elif percentage >= 70:
        return 8.0
    elif percentage >= 60:
        return 7.0
    elif percentage >= 50:
        return 6.0
    else:
        return 0.0


def get_remark(percentage):
    """Return a motivational remark based on performance."""
    if percentage >= 90:
        return "Outstanding! Keep it up!"
    elif percentage >= 80:
        return "Excellent work!"
    elif percentage >= 70:
        return "Good job! Room to grow."
    elif percentage >= 60:
        return "Average. Push a little harder!"
    elif percentage >= 50:
        return "Passed, but aim higher next time."
    else:
        return "Failed. Don't give up - study harder!"


def print_separator(char="-", length=45):
    print(char * length)


def main():
    print_separator("=")
    print("     STUDENT GRADE CALCULATOR")
    print("     By Niyati Shah | B.Tech CSE")
    print_separator("=")

    # Get student name
    name = input("\nEnter student name: ").strip()
    if not name:
        name = "Student"

    # Get number of subjects
    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Collect marks for each subject
    subjects = []
    marks = []
    max_marks = []

    print_separator()
    print("Enter subject details:")
    print_separator()

    for i in range(1, num_subjects + 1):
        subject = input(f"Subject {i} name: ").strip()
        if not subject:
            subject = f"Subject {i}"

        while True:
            try:
                max_mark = int(input(f"  Max marks for {subject}: "))
                if max_mark <= 0:
                    print("  Max marks must be positive.")
                else:
                    break
            except ValueError:
                print("  Invalid input. Enter a number.")

        while True:
            try:
                mark = float(input(f"  Marks obtained in {subject}: "))
                if mark < 0 or mark > max_mark:
                    print(f"  Marks must be between 0 and {max_mark}.")
                else:
                    break
            except ValueError:
                print("  Invalid input. Enter a number.")

        subjects.append(subject)
        marks.append(mark)
        max_marks.append(max_mark)
        print()

    # Calculate results
    total_obtained = sum(marks)
    total_maximum = sum(max_marks)
    percentage = (total_obtained / total_maximum) * 100
    grade = get_grade(percentage)
    gpa = get_gpa(percentage)
    remark = get_remark(percentage)
    passed_all = all(
        (marks[i] / max_marks[i]) * 100 >= 50 for i in range(num_subjects)
    )

    # Display result report
    print_separator("=")
    print(f"       RESULT CARD — {name.upper()}")
    print_separator("=")

    print(f"\n{'Subject':<20} {'Max':>6} {'Obtained':>10} {'%':>8} {'Grade':>6}")
    print_separator()

    for i in range(num_subjects):
        subj_pct = (marks[i] / max_marks[i]) * 100
        subj_grade = get_grade(subj_pct)
        status = " ✗" if subj_pct < 50 else ""
        print(f"{subjects[i]:<20} {max_marks[i]:>6} {marks[i]:>10.1f} {subj_pct:>7.1f}% {subj_grade:>5}{status}")

    print_separator()
    print(f"{'TOTAL':<20} {total_maximum:>6} {total_obtained:>10.1f} {percentage:>7.1f}%")
    print_separator("=")

    print(f"\n  Overall Grade  : {grade}")
    print(f"  GPA (10 scale) : {gpa:.1f}")
    print(f"  Result         : {'PASS ✓' if passed_all else 'FAIL ✗'}")
    print(f"  Remark         : {remark}")

    print_separator("=")

    # Save report to file
    save = input("\nSave report to file? (yes/no): ").strip().lower()
    if save in ("yes", "y"):
        filename = f"{name.replace(' ', '_')}_result.txt"
        with open(filename, "w") as f:
            f.write(f"STUDENT GRADE REPORT\n")
            f.write(f"Name: {name}\n")
            f.write(f"=" * 45 + "\n")
            f.write(f"{'Subject':<20} {'Max':>6} {'Obtained':>10} {'%':>8} {'Grade':>6}\n")
            f.write("-" * 45 + "\n")
            for i in range(num_subjects):
                subj_pct = (marks[i] / max_marks[i]) * 100
                subj_grade = get_grade(subj_pct)
                f.write(f"{subjects[i]:<20} {max_marks[i]:>6} {marks[i]:>10.1f} {subj_pct:>7.1f}% {subj_grade:>5}\n")
            f.write("-" * 45 + "\n")
            f.write(f"Overall %  : {percentage:.1f}%\n")
            f.write(f"Grade      : {grade}\n")
            f.write(f"GPA        : {gpa:.1f}/10\n")
            f.write(f"Result     : {'PASS' if passed_all else 'FAIL'}\n")
        print(f"\n  Report saved as '{filename}' ✓")

    print("\nThank you for using Grade Calculator!")
    print_separator("=")


if __name__ == "__main__":
    main()
