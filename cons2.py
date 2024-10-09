import sqlite3


connection = sqlite3.connect('checkcinstraint.db')
cursor = connection.cursor()





create_query = """
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    CONSTRAINT price_check CHECK (price > 0)
);
"""


cursor.execute(create_query)


connection.commit()

products = [
    ('phone', 50),
    ('headphones', -100)   
]


try:
    for product in products:
        cursor.execute("INSERT INTO products (product_name, price) VALUES (?, ?)", product)
    connection.commit()
except sqlite3.IntegrityError as e:
    print("IntegrityError occurred:", e)


connection.close()
