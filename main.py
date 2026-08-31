from database import create_table
from student_manager import (
    add_student,
    get_all_students,
    get_student_by_roll_no,
    update_student,
    delete_student
)


def add_student_menu():

    name = input("Enter student name: ")

    roll_no = input("Enter roll number: ")

    department = input("Enter department: ")


    while True:

        try:

            marks = int(input("Enter marks: "))

            if 0 <= marks <= 100:
                break

            print("Marks must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


    try:

        add_student(name, roll_no, department, marks)

        print("Student added successfully!")

    except Exception:

        print("Roll number already exists.")


def view_students_menu():

    students = get_all_students()


    if not students:

        print("No students found.")

        return


    print("\n===== Student Details =====")


    for student in students:

        print("ID:", student[0])
        print("Name:", student[1])
        print("Roll Number:", student[2])
        print("Department:", student[3])
        print("Marks:", student[4])

        print("----------------------")


def search_student_menu():

    roll_no = input("Enter roll number to search: ")


    student = get_student_by_roll_no(roll_no)


    if student:

        print("\nStudent Found!")

        print("ID:", student[0])
        print("Name:", student[1])
        print("Roll Number:", student[2])
        print("Department:", student[3])
        print("Marks:", student[4])

    else:

        print("Student not found.")


def update_student_menu():

    roll_no = input("Enter roll number to update: ")


    student = get_student_by_roll_no(roll_no)


    if not student:

        print("Student not found.")

        return


    name = input("Enter new name: ")

    department = input("Enter new department: ")


    while True:

        try:

            marks = int(input("Enter new marks: "))

            if 0 <= marks <= 100:
                break

            print("Marks must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


    update_student(
        roll_no,
        name,
        department,
        marks
    )


    print("Student updated successfully!")


def delete_student_menu():

    roll_no = input("Enter roll number to delete: ")


    student = get_student_by_roll_no(roll_no)


    if not student:

        print("Student not found.")

        return


    delete_student(roll_no)


    print("Student deleted successfully!")


def main():

    create_table()


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

            add_student_menu()


        elif choice == "2":

            view_students_menu()


        elif choice == "3":

            search_student_menu()


        elif choice == "4":

            update_student_menu()


        elif choice == "5":

            delete_student_menu()


        elif choice == "6":

            print("Thank you for using Student Management System!")

            break


        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()