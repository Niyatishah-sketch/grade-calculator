# ============================================
#   Student Grade Calculator
#   Author: Niyati Shah
#   B.Tech CSE, Indus University
# ============================================

def grade_calculator(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks = int(input("Enter your marks: "))
print("Grade:", grade_calculator(marks))



