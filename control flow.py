temperature = 30

if temperature > 25:
    print("It’s a hot day! ☀️")
else:
    print("It’s a cool day! ❄️")

    # Control flow example for grading student marks
# This will ask the user for input and grade the student's performance

# Prompt the user for student marks
marks = int(input("Enter the student's marks (0-100): "))
marks = int(65)
# Grading system based on the marks
if marks > 70:
    print("Grade: Distinction 🏆")
elif marks >= 60:
    print("Grade: Credit 🎖️")
elif marks >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: Fail ❌")