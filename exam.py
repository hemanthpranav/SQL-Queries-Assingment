import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_database.db')

# Enable foreign key constraint enforcement
conn.execute("PRAGMA foreign_keys = ON;")

# Create a cursor object
cursor = conn.cursor()

# SQL query to create students table
create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL
);
"""

# SQL query to create courses table
create_courses_table = """
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER NOT NULL,
    course_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    PRIMARY KEY (course_id, department_id)
);
"""

# SQL query to create student_courses table with foreign keys
create_student_courses_table = """
CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id, department_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id, department_id) REFERENCES courses(course_id, department_id) ON DELETE CASCADE
);
"""

# Execute the queries to create tables
cursor.execute(create_students_table)
cursor.execute(create_courses_table)
cursor.execute(create_student_courses_table)

# Commit the changes
conn.commit()

# Insert data into students and courses
cursor.execute("INSERT INTO students (student_name) VALUES ('John Doe')")
cursor.execute("INSERT INTO courses (course_id, course_name, department_id) VALUES (1, 'Mathematics', 101)")

# Valid entry in student_courses
try:
    cursor.execute("INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 1, 101)")
    conn.commit()
    print("Valid entry inserted into student_courses")
except sqlite3.IntegrityError as e:
    print("IntegrityError occurred for valid entry:", e)

# Invalid entry (student_id does not exist)
try:
    cursor.execute("INSERT INTO student_courses (student_id, course_id, department_id) VALUES (999, 1, 101)")  # Invalid student_id
    conn.commit()
except sqlite3.IntegrityError as e:
    print("IntegrityError occurred for invalid student_id:", e)

# Invalid entry (course_id does not exist)
try:
    cursor.execute("INSERT INTO student_courses (student_id, course_id, department_id) VALUES (1, 999, 101)")  # Invalid course_id
    conn.commit()
except sqlite3.IntegrityError as e:
    print("IntegrityError occurred for invalid course_id:", e)

# Close the connection
conn.close()python