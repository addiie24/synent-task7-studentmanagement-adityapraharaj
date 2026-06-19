import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except:
            return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!\n")


def view_students():
    students = load_students()

    if not students:
        print("No students found.\n")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )

    print()


def update_student():
    students = load_students()

    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            student["course"] = input("New Course: ")

            save_students(students)

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def menu():
    while True:

        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.\n")


menu()