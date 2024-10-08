import sqlite3
from tabulate import tabulate


connection = sqlite3.connect('JoinwithAggregation.db')
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
        product_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
''')







cursor.execute("INSERT INTO customers (customer_name) VALUES ('CLARK')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('HEMANTH')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('BRUCE')")

cursor.execute("INSERT INTO orders (customer_id, product_id) VALUES (1, 11)")  
cursor.execute("INSERT INTO orders (customer_id, product_id) VALUES (1, 12)")  
cursor.execute("INSERT INTO orders (customer_id, product_id) VALUES (2, 11)")  
cursor.execute("INSERT INTO orders (customer_id, product_id) VALUES (2, 13)") 
cursor.execute("INSERT INTO orders (customer_id, product_id) VALUES (3, 14)")  


connection.commit()


query = '''
    SELECT 
        c.customer_name,
        COUNT(o.order_id) AS total_orders
    FROM 
        customers c
    LEFT JOIN 
        orders o ON c.customer_id = o.customer_id
    GROUP BY 
        c.customer_name;
'''


cursor.execute(query)


cross_join = cursor.fetchall()


headings = ['Customer Name', 'Total Products Ordered']
final = cross_join 

print("\n total orders:")
print(tabulate(final, headers=headings, tablefmt='grid'))
connection.close()