from database import get_connection


def add_student(name, roll_no, department, marks):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students
    (name, roll_no, department, marks)
    VALUES (?, ?, ?, ?)
    """, (name, roll_no, department, marks))

    connection.commit()

    connection.close()


def get_all_students():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    return students


def get_student_by_roll_no(roll_no):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    connection.close()

    return student


def update_student(roll_no, name, department, marks):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    UPDATE students
    SET name = ?, department = ?, marks = ?
    WHERE roll_no = ?
    """, (name, department, marks, roll_no))

    connection.commit()

    connection.close()


def delete_student(roll_no):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    connection.commit()

    connection.close()