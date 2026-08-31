import sqlite3


DATABASE_NAME = "students.db"


def get_connection():

    return sqlite3.connect(DATABASE_NAME)


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

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

    connection.close()