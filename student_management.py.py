import json


FILE_NAME = "students.json"


class Student:

    def __init__(self, name, roll_no, department, marks):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.marks = marks


students = []


def save_students():

    data = []

    for student in students:

        data.append({
            "name": student.name,
            "roll_no": student.roll_no,
            "department": student.department,
            "marks": student.marks
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_students():

    try:

        with open(FILE_NAME, "r") as file:

            data = json.load(file)

            for item in data:

                student = Student(
                    item["name"],
                    item["roll_no"],
                    item["department"],
                    item["marks"]
                )

                students.append(student)

    except FileNotFoundError:

        print("No existing student data found.")

    except json.JSONDecodeError:

        print("Student data file is corrupted.")


def add_student():

    while True:

        name = input("Enter student name: ")

        if name.strip() != "":
            break

        print("Name cannot be empty.")


    while True:

        roll_no = input("Enter roll number: ")

        if roll_no.strip() == "":
            print("Roll number cannot be empty.")
            continue

        duplicate = False

        for student in students:

            if student.roll_no == roll_no:
                duplicate = True
                break

        if duplicate:
            print("Roll number already exists.")

        else:
            break


    while True:

        department = input("Enter department: ")

        if department.strip() != "":
            break

        print("Department cannot be empty.")


    while True:
        try:
            marks = int(input("Enter marks: "))

            if 0 <= marks <= 100:
                break

            else:
                print("Marks must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


    student = Student(
        name,
        roll_no,
        department,
        marks
    )

    students.append(student)

    save_students()

    print("Student added successfully!")


def view_students():

    if len(students) == 0:

        print("No students found.")

    else:

        print("\n===== Student Details =====")

        for student in students:

            print("Name:", student.name)
            print("Roll Number:", student.roll_no)
            print("Department:", student.department)
            print("Marks:", student.marks)

            print("----------------------")


def search_student():

    roll_no = input("Enter roll number to search: ")

    found = False

    for student in students:

        if student.roll_no == roll_no:

            print("\nStudent Found!")

            print("Name:", student.name)
            print("Roll Number:", student.roll_no)
            print("Department:", student.department)
            print("Marks:", student.marks)

            found = True
            break

    if found == False:

        print("Student not found.")


def update_student():

    roll_no = input("Enter roll number to update: ")

    found = False

    for student in students:

        if student.roll_no == roll_no:

            print("\nEnter new details:")

            student.name = input("Enter new name: ")
            student.department = input("Enter new department: ")

            while True:
                try:
                    marks = input("Enter new marks: ")

                    if marks.isdigit():

                        marks = int(marks)

                    if 0 <= marks <= 100:
                        student.marks = marks
                        break

                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

            save_students()

            print("Student updated successfully!")

            found = True
            break

    if found == False:

        print("Student not found.")


def delete_student():

    roll_no = input("Enter roll number to delete: ")

    found = False

    for student in students:

        if student.roll_no == roll_no:

            students.remove(student)

            save_students()

            print("Student deleted successfully!")

            found = True
            break

    if found == False:

        print("Student not found.")


load_students()


while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        add_student()


    elif choice == "2":

        view_students()


    elif choice == "3":

        search_student()


    elif choice == "4":

        update_student()


    elif choice == "5":

        delete_student()


    elif choice == "6":

        print("Thank you for using Student Management System!")

        break


    else:

        print("Invalid choice.")