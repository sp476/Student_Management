import json
import os

FILE_NAME = "students.json"


def load_students():
    """Load student records from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read student records. Starting with an empty list.")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def get_valid_marks(prompt):
    """Ask for marks between 0 and 100."""
    try:
        marks = float(input(prompt))
        if 0 <= marks <= 100:
            return marks
        print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")
    return None


def add_student():
    students = load_students()
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"] == student_id:
            print("That student ID already exists.")
            return

    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    marks = get_valid_marks("Enter marks (0-100): ")
    if marks is None:
        return

    students.append({"id": student_id, "name": name, "marks": marks})
    save_students(students)
    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']}"
        )


def search_student():
    students = load_students()
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent found:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            return

    print("Student not found.")


def update_marks():
    students = load_students()
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            marks = get_valid_marks("Enter new marks (0-100): ")
            if marks is None:
                return

            student["marks"] = marks
            save_students(students)
            print("Marks updated successfully!")
            return

    print("Student not found.")


def delete_student():
    students = load_students()
    student_id = input("Enter student ID to delete: ").strip()

    for index, student in enumerate(students):
        if student["id"] == student_id:
            confirm = input(
                f"Delete {student['name']}? Type yes to confirm: "
            ).strip().lower()

            if confirm == "yes":
                students.pop(index)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


def show_average_marks():
    students = load_students()

    if not students:
        print("No student records available.")
        return

    average = sum(student["marks"] for student in students) / len(students)
    print(f"Average marks: {average:.2f}")


def show_top_student():
    students = load_students()

    if not students:
        print("No student records available.")
        return

    top_student = max(students, key=lambda student: student["marks"])
    print(
        f"Top student: {top_student['name']} "
        f"(ID: {top_student['id']}, Marks: {top_student['marks']})"
    )


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student marks")
        print("5. Delete student")
        print("6. Show average marks")
        print("7. Show top student")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_average_marks()
        elif choice == "7":
            show_top_student()
        elif choice == "8":
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
