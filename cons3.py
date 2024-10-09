import sqlite3


connection = sqlite3.connect('primaryconstraint.db')
cursor = connection.cursor()





create_query = """
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER NOT NULL,
    course_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    PRIMARY KEY (course_id, department_id)
);
"""


cursor.execute(create_query)


connection.commit()

courses = [
    (1, 'Maths', 101),  
    (2, 'Physics', 101),      
    (1, 'Advanced Maths', 101) 
]


try:
    for course in courses:
        cursor.execute("INSERT INTO courses (course_id, course_name, department_id) VALUES (?, ?, ?)", course)
    connection.commit()
except sqlite3.IntegrityError as e:
    print("Error occurred duplicate course_id:", e)


connection.close()

connection.close()
