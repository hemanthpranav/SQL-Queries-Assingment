import sqlite3
from tabulate import tabulate


connection = sqlite3.connect('Multiplejoins.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
''')






cursor.execute("INSERT INTO customers (customer_name) VALUES ('CLARK')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('HEMANTH')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('BRUCE')")

cursor.execute("INSERT INTO products (product_name) VALUES ('tv')")
cursor.execute("INSERT INTO products (product_name) VALUES ('iphone')")
cursor.execute("INSERT INTO products (product_name) VALUES ('macbook')")

cursor.execute("INSERT INTO orders (customer_id, product_id, order_date) VALUES (1, 1, '2023-07-05')")  
cursor.execute("INSERT INTO orders (customer_id, product_id, order_date) VALUES (2, 1, '2024-06-04')")  
cursor.execute("INSERT INTO orders (customer_id, product_id, order_date) VALUES (1, 2, '2023-08-05')")  
cursor.execute("INSERT INTO orders (customer_id, product_id, order_date) VALUES (3, 3, '2024-09-09')")   


connection.commit()


query = '''
    SELECT 
        c.customer_name,
        p.product_name,
        o.order_date
    FROM 
        orders o
    JOIN 
        customers c ON o.customer_id = c.customer_id
    JOIN 
        products p ON o.product_id = p.product_id;
'''


cursor.execute(query)


join = cursor.fetchall()


headings = ['Customer Name', 'Product Name', 'Order Date']
final = join 

print("\n Multiple joins:")
print(tabulate(final, headers=headings, tablefmt='grid'))
connection.close()