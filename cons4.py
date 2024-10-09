import sqlite3


connection = sqlite3.connect('foreignkeyconstraint.db')
connection.execute("PRAGMA foreign_keys = ON;")
cursor = connection.cursor()





students_table = """
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL
);
"""


courses_table = """
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER NOT NULL,
    course_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    PRIMARY KEY (course_id, department_id)
);
"""


student_courses_table = """
CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id, department_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id, department_id) REFERENCES courses(course_id, department_id) ON DELETE CASCADE
);
"""


cursor.execute(students_table)
cursor.execute(courses_table)
cursor.execute(student_courses_table)


connection.commit()

cursor.execute("INSERT INTO students (student_name) VALUES ('zack snyder')")
cursor.execute("INSERT INTO courses (course_id, course_name, department_id) VALUES (1, 'database', 101)")


try:
    cursor.execute("INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 1, 101)")
    connection.commit()
    print("Valid entry inserted into student_courses")
except sqlite3.IntegrityError as e:
    print("IntegrityError :", e)


try:
    cursor.execute("INSERT INTO student_courses (student_id, course_id, department_id) VALUES (999, 1, 101)")  # Invalid student_id
    connection.commit()
except sqlite3.IntegrityError as e:
    print("Error occurred for invalid student_id:", e)


try:
    cursor.execute("INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 999, 101)")  # Invalid course_id
    connection.commit()
except sqlite3.IntegrityError as e:
    print("Error occurred for invalid course_id:", e)


connection.close()
