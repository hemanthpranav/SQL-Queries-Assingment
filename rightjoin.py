import sqlite3

from tabulate import tabulate
conn = sqlite3.connect('right.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS product_suppliers (
    product_id INTEGER,
    supplier_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
)
''')


cursor.execute("INSERT INTO products (product_name) VALUES ('phone')")
cursor.execute("INSERT INTO products (product_name) VALUES ('Bicuits')")
cursor.execute("INSERT INTO products (product_name) VALUES ('Cats')")
cursor.execute("INSERT INTO products (product_name) VALUES ('Dogs')")

# Insert sample data into suppliers
cursor.execute("INSERT INTO suppliers (supplier_name) VALUES ('amazon')")
cursor.execute("INSERT INTO suppliers (supplier_name) VALUES ('flipkart')")


cursor.execute("INSERT INTO product_suppliers (product_id, supplier_id) VALUES (1, 1)")
cursor.execute("INSERT INTO product_suppliers (product_id, supplier_id) VALUES (1, 2)")
cursor.execute("INSERT INTO product_suppliers (product_id, supplier_id) VALUES (2, 1)")



conn.commit()


query = '''
SELECT p.product_id, p.product_name, s.supplier_id, s.supplier_name
FROM products p
LEFT JOIN product_suppliers ps ON p.product_id = ps.product_id
LEFT JOIN suppliers s ON ps.supplier_id = s.supplier_id;
'''


cursor.execute(query)


results = cursor.fetchall()

table_headers = ['Product ID', 'Product Name', 'Supplier ID', 'Supplier Name']
table = [list(row) for row in results]  


print(tabulate(table, headers=table_headers, tablefmt='grid'))

cursor.close()
conn.close()