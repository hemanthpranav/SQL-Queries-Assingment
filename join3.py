import sqlite3
import pandas as pd

from tabulate import tabulate

connection = sqlite3.connect('Innerjoin.db')


cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        manager_id INTEGER,
        FOREIGN KEY (manager_id) REFERENCES employees(employee_id) 
               )
''')




cursor.execute("INSERT INTO employees (employee_name, manager_id) VALUES ('Hemanth',NULL)")
cursor.execute("INSERT INTO employees (employee_name, manager_id) VALUES ('zack', 1)")
cursor.execute("INSERT INTO employees (employee_name, manager_id) VALUES ('Bruce', 1)")


cursor.execute("INSERT INTO employees (employee_name, manager_id) VALUES ('Clark', 2)")  
cursor.execute("INSERT INTO employees (employee_name, manager_id) VALUES ('Alfred', 2)")  



connection.commit()


innerjoin = '''
    SELECT e.employee_name , m.employee_name AS manager 
FROM employees e INNER JOIN employees m ON e.manager_id = m.employee_id;

'''

df = pd.read_sql_query(innerjoin, connection)


df.fillna('None', inplace=True)


print("\nEmployee and Manager List:")
print(df)


connection.close()