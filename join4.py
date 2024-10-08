import sqlite3

from tabulate import tabulate

connection = sqlite3.connect('crossjoin.db')


cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    )
''')



cursor.execute("INSERT INTO products (product_name) VALUES ('TV')")
cursor.execute("INSERT INTO products (product_name) VALUES ('IPHONE')")
cursor.execute("INSERT INTO products (product_name) VALUES ('HEADPHONES')")


cursor.execute("INSERT INTO customers (customer_name) VALUES ('PRANAV')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('ZACK')")
cursor.execute("INSERT INTO customers (customer_name) VALUES ('BRUCE')")


connection.commit()


crossjoin = '''
    SELECT 
        p.product_name,
        c.customer_name
    FROM 
        products p
    CROSS JOIN 
        customers c;
'''

cursor.execute(crossjoin)

results = cursor.fetchall()


headers = ['Product Name', 'Customer Name']
data = results 

print("\n CROSS JOIN:")
print(tabulate(data, headers=headers, tablefmt='grid'))

connection.close()