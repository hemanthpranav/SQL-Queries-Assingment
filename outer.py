import sqlite3
from tabulate import tabulate


conn = sqlite3.connect('outer.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
)
''')


cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM departments")


cursor.execute("INSERT INTO departments (department_name) VALUES ('marketing')")
cursor.execute("INSERT INTO departments (department_name) VALUES ('Pantry')")
cursor.execute("INSERT INTO departments (department_name) VALUES ('Sales')")


cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('pranav', 1)")
cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('Bruce', 1)")
cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('Clark', 2)")

cursor.execute("INSERT INTO employees (employee_name, department_id) VALUES ('lex', NULL)")


conn.commit()


sql_query = '''
SELECT e.employee_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id

UNION

SELECT e.employee_name, d.department_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;
'''


cursor.execute(sql_query)


results = cursor.fetchall()


table_headers = ['Employee Name', 'Department Name']
table = [list(row) for row in results] 


print(tabulate(table, headers=table_headers, tablefmt='grid'))


cursor.close()
conn.close()