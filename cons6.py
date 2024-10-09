import sqlite3


connection = sqlite3.connect('check.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        salary REAL CHECK (salary > 0)
    )
''')


cursor.execute('INSERT INTO employees (employee_name, salary) VALUES ("zack", 980000)')
cursor.execute('INSERT INTO employees (employee_name, salary) VALUES ("pran", 57500)')
cursor.execute('INSERT INTO employees (employee_name, salary) VALUES ("clark", 0)') 
connection.commit()




connection.close()