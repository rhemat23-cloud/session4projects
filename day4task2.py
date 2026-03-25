def get_marks(subject):
    """Safely get marks for a subject (0-100)."""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print(" Marks must be between 0 and 100.")
        except ValueError:
            print(" Invalid input. Please enter a number.")

def calculate_grade(percentage):
    """Assign grade based on percentage."""
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

def generate_report(student_name, roll_no, marks_dict):
    """Generate and print the student report card."""
    total_marks = sum(marks_dict.values())
    percentage = total_marks / len(marks_dict)
    grade = calculate_grade(percentage)

    print("\n" + "="*40)
    print("        STUDENT REPORT CARD")
    print("="*40)
    print(f"Name       : {student_name}")
    print(f"Roll No.   : {roll_no}")
    print("-"*40)
    for subject, marks in marks_dict.items():
        print(f"{subject:<15}: {marks:>5}")
    print("-"*40)
    print(f"Total Marks: {total_marks:.2f}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print("="*40)

if __name__ == "__main__":
    print(" Student Report Card Generator ")
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()

    subjects = ["Maths", "Science", "English"]
    marks = {subject: get_marks(subject) for subject in subjects}

    generate_report(name, roll_no, marks)
