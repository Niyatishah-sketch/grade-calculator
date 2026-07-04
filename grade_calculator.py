# ============================================
#   Student Grade Calculator
#   Author: Niyati Shah
#   B.Tech CSE, Indus University
# ============================================
def get_grade_point(marks):
    """Convert marks (out of 100) to a grade point (0-10 scale)."""
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    else:
        return 0


def get_letter_grade(marks):
    """Convert marks to a letter grade for display."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


def calculate_cgpa(subjects):
    """
    subjects: list of dicts, each with 'name', 'credits', 'marks'
    Returns overall CGPA using credit-weighted average across all subjects.
    """
    total_credits = 0
    total_points = 0

    print(f"\n{'Subject':<20}{'Credits':<10}{'Marks':<10}{'Grade':<10}{'Grade Point':<12}")
    print("-" * 62)

    for subject in subjects:
        grade_point = get_grade_point(subject["marks"])
        letter_grade = get_letter_grade(subject["marks"])
        total_credits += subject["credits"]
        total_points += subject["credits"] * grade_point

        print(f"{subject['name']:<20}{subject['credits']:<10}{subject['marks']:<10}"
              f"{letter_grade:<10}{grade_point:<12}")

    if total_credits:
        cgpa = round(total_points / total_credits, 2)
    else:
        cgpa = 0

    return cgpa


def main():
    print("=== CGPA Calculator ===")
    num_subjects = int(input("Enter total number of subjects: "))
    subjects = []

    for i in range(num_subjects):
        name = input(f"Subject {i + 1} name: ")
        credits = int(input(f"Credits for {name}: "))
        marks = int(input(f"Marks obtained (out of 100) for {name}: "))
        subjects.append({"name": name, "credits": credits, "marks": marks})

    cgpa = calculate_cgpa(subjects)
    print("\n=== Final Result ===")
    print(f"Overall CGPA: {cgpa}")


if __name__ == "__main__":
    main()

  



