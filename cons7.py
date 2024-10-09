import sqlite3


conn = sqlite3.connect('composite.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),  -- Composite key constraint
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (course_id) REFERENCES courses (course_id)
    )
''')


cursor.execute('INSERT INTO students (student_name) VALUES ("pranav")')
cursor.execute('INSERT INTO students (student_name) VALUES ("zack")')
cursor.execute('INSERT INTO courses (course_name) VALUES ("database 101")')
cursor.execute('INSERT INTO courses (course_name) VALUES ("science 201")')


cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 1)')  
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (2, 2)')  


try:
    cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (1, 1)')  
except sqlite3.IntegrityError as e:
    print("Error  duplicate entry into student_courses:", e)



conn.commit()
conn.close()