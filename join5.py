import sqlite3
from tabulate import tabulate


connection = sqlite3.connect('naturaljoin.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
''')







cursor.execute("INSERT INTO customers (customer_name) VALUES ('CLARK')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('HEMANTH')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('BRUCE')")


cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (1, '2023-05-01')")
cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (1, '2024-07-03')")
cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (2, '2023-08-06')")
cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (3, '2023-09-04')")


connection.commit()


query = '''
    SELECT 
        customer_name,
        order_id,
        order_date
    FROM 
        customers
    NATURAL JOIN 
        orders;
'''


cursor.execute(query)


cross_join = cursor.fetchall()


headings = ['Customer Name', 'Order ID', 'Order Date']
final = cross_join 

print("\nList of Customers and Their Orders (NATURAL JOIN):")
print(tabulate(final, headers=headings, tablefmt='grid'))
connection.close()