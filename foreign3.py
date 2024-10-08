import sqlite3


connection = sqlite3.connect('violatingforeignkeys.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")



cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
''')


cursor.execute("INSERT INTO customers (customer_name) VALUES ('Pranav')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('Bruce')")


connection.commit()


try:
    cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (4, '2023-12-18')")  
    connection.commit()
except sqlite3.IntegrityError as e:
    print("Error customer_id does not exist:", e) 


connection.close()