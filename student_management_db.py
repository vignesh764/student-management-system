import sqlite3


# -----------------------------
# Database Connection
# -----------------------------

connection = sqlite3.connect("students.db")
cursor = connection.cursor()


# -----------------------------
# Create Table
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")

connection.commit()


# -----------------------------
# Add Student
# -----------------------------

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

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        existing_student = cursor.fetchone()

        if existing_student:

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


    cursor.execute("""
    INSERT INTO students
    (name, roll_no, department, marks)
    VALUES (?, ?, ?, ?)
    """, (name, roll_no, department, marks))

    connection.commit()

    print("Student added successfully!")


# -----------------------------
# View Students
# -----------------------------

def view_students():

    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()


    if len(records) == 0:

        print("No students found.")

    else:

        print("\n===== Student Details =====")

        for student in records:

            print("ID:", student[0])
            print("Name:", student[1])
            print("Roll Number:", student[2])
            print("Department:", student[3])
            print("Marks:", student[4])

            print("----------------------")


# -----------------------------
# Search Student
# -----------------------------

def search_student():

    roll_no = input("Enter roll number to search: ")


    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()


    if student:

        print("\nStudent Found!")

        print("ID:", student[0])
        print("Name:", student[1])
        print("Roll Number:", student[2])
        print("Department:", student[3])
        print("Marks:", student[4])

    else:

        print("Student not found.")


# -----------------------------
# Update Student
# -----------------------------

def update_student():

    roll_no = input("Enter roll number to update: ")


    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()


    if student:

        print("\nEnter new details:")

        name = input("Enter new name: ")
        department = input("Enter new department: ")


        while True:

            try:

                marks = int(input("Enter new marks: "))

                if 0 <= marks <= 100:
                    break

                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:

                print("Please enter a valid number.")


        cursor.execute("""
        UPDATE students
        SET name = ?, department = ?, marks = ?
        WHERE roll_no = ?
        """, (name, department, marks, roll_no))

        connection.commit()

        print("Student updated successfully!")

    else:

        print("Student not found.")


# -----------------------------
# Delete Student
# -----------------------------

def delete_student():

    roll_no = input("Enter roll number to delete: ")


    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()


    if student:

        cursor.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        connection.commit()

        print("Student deleted successfully!")

    else:

        print("Student not found.")


# -----------------------------
# Main Menu
# -----------------------------

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


# Close database connection

connection.close()