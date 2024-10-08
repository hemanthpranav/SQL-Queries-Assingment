import sqlite3

from tabulate import tabulate

conn = sqlite3.connect('innerjoin.db')


cursor = conn.cursor()


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
        product_name TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
''')


cursor.execute("INSERT INTO customers (customer_name) VALUES ('Hemanth Pranav')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('Zack snyder')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('Bruce Wayne')")


cursor.execute("INSERT INTO orders (customer_id, product_name) VALUES (1, 'Headphone')")
cursor.execute("INSERT INTO orders (customer_id, product_name) VALUES (1, 'Keyboard')")
cursor.execute("INSERT INTO orders (customer_id, product_name) VALUES (2, 'Mouse')")
cursor.execute("INSERT INTO orders (customer_id, product_name) VALUES (3, 'Televison')")


conn.commit()


cursor.execute('''
    SELECT customers.customer_name, orders.product_name
    FROM customers
    JOIN orders ON customers.customer_id = orders.customer_id
''')


table_a = cursor.fetchall()


heading = ["Customer", "Product"]
print(tabulate(table_a, heading, tablefmt="grid"))


conn.close()