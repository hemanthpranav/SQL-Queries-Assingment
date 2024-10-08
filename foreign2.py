import sqlite3
from tabulate import tabulate


connection = sqlite3.connect('CascadingDeletes.db')
cursor = connection.cursor()


cursor.execute('''
  CREATE TABLE categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT NOT NULL
    
    )
''')


cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
               )
''')



cursor.execute("INSERT INTO categories (category_name) VALUES ('Mobiles')")
cursor.execute("INSERT INTO categories (category_name) VALUES ('tv')")
cursor.execute("INSERT INTO categories (category_name) VALUES ('headphones')")

cursor.execute("INSERT INTO products (product_name, category_id) VALUES ('galaxy', 1)")
cursor.execute("INSERT INTO products (product_name, category_id) VALUES ('iphone', 1)")
cursor.execute("INSERT INTO products (product_name, category_id) VALUES ('Sony', 2)")
cursor.execute("INSERT INTO products (product_name, category_id) VALUES ('Bose', 3)")

connection.commit()


query = '''
 SELECT 
        c.category_name, 
        p.product_name 
    FROM 
        categories c
    LEFT JOIN 
        products p ON c.category_id = p.category_id;
'''


cursor.execute(query)


foreign = cursor.fetchall()


headings = ['Category Name', 'Product Name']
final = foreign

print("\nProducts and categories before their deletion:")
print(tabulate(final, headers=headings, tablefmt='grid'))

cursor.execute("DELETE FROM categories WHERE category_id = 1")  # Deleting the 'Electronics' category

# Commit the changes
connection.commit()

# Query to display categories and their products after deletion
cursor.execute(query)
results_after_deletion = cursor.fetchall()

# Display the results after deletion
print("\nProducts and categories before their deletion of MOBILES:")
print(tabulate(results_after_deletion, headers=headings, tablefmt='grid'))


connection.close()