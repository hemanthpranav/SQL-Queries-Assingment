import sqlite3


connection = sqlite3.connect('uniquecinstraint.db')
cursor = connection.cursor()





create_query = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL,
    CONSTRAINT email_unique UNIQUE (email)
);
"""


cursor.execute(create_query)


connection.commit()

# Test data
users = [
    ('pranav', 'pranav@example.com'),
    ('zack', 'zack@snyder.com'),
    ('bruce', 'pranav@example.com')  # This should cause an error
]


try:
    for user in users:
        cursor.execute("INSERT INTO users (user_name, email) VALUES (?, ?)", user)
    connection.commit()
except sqlite3.IntegrityError as e:
    print("Error occurred. Email already exists:", e)


connection.close()

