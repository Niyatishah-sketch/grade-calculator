# CGPA Calculator (Python)

A simple command-line Python program that calculates a student's **CGPA **(Cumulative Grade Point Average)** using a credit-weighted average — the same method most universities use for grading.

## Features

- Accepts subject-wise **credits** and **marks** as input
- Automatically converts marks into **grade points** (0–10 scale) and **letter grades** (A+, A, B, C, D, E, F)
- Calculates CGPA using the formula:

  ```
  CGPA = (Sum of Credits × Grade Points for all subjects) / (Total Credits)
  ```

- Displays a clean summary table of all subjects, credits, marks, and grades
- Handles edge cases (e.g., avoids division by zero if no credits are entered)

## How It Works

1. The program asks how many subjects you want to enter.
2. For each subject, it asks for:
   - Subject name
   - Credits
   - Marks obtained (out of 100)
3. Marks are converted into grade points using this scale:

   | Marks Range | Grade Point | Letter Grade |
   |---|---|---|
   | 90 - 100 | 10 | A+ |
   | 80 - 89  | 9  | A  |
   | 70 - 79  | 8  | B  |
   | 60 - 69  | 7  | C  |
   | 50 - 59  | 6  | D  |
   | 40 - 49  | 5  | E  |
   | Below 40 | 0  | F  |

4. Each subject's credits and grade points are used to calculate a **credit-weighted CGPA**, so subjects with higher credits have a proportionally larger impact on the final result.

## How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/cgpa-calculator-python.git
   cd cgpa-calculator-python
   ```
3. Run the script:
   ```bash
   python cgpa_calculator_direct.py
   ```
4. Follow the on-screen prompts to enter your subjects, credits, and marks.

## Sample Output

```
=== CGPA Calculator ===
Enter total number of subjects: 3
Subject 1 name: Maths
Credits for Maths: 4
Marks obtained (out of 100) for Maths: 85
Subject 2 name: Physics
Credits for Physics: 3
Marks obtained (out of 100) for Physics: 72
Subject 3 name: English
Credits for English: 2
Marks obtained (out of 100) for English: 65

Subject             Credits   Marks     Grade     Grade Point
--------------------------------------------------------------
Maths               4         85        A         9
Physics              3         72        B         8
English              2         65        C         7

=== Final Result ===
Overall CGPA: 8.22
```

## Tech Stack

- **Language:** Python 3
- **Concepts used:** Functions, conditionals, loops, dictionaries, string formatting, input validation

## Future Improvements

- Add support for semester-wise SGPA and overall CGPA across semesters
- Build a simple GUI (using Tkinter) or web version (using Flask)
- Add input validation for invalid marks/credits (e.g., negative numbers)
- Export results to a CSV or PDF report



**Niyati Shah**
B.Tech Computer Science, Indus University
📧 shahniyati643@gmail.com
