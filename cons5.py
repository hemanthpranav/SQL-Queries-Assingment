import sqlite3


connection = sqlite3.connect('nonullconstraint.db')
connection.execute("PRAGMA foreign_keys = ON;")
cursor = connection.cursor()





table = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL

);
"""





cursor.execute(table)






try:
    cursor.execute("INSERT INTO users (username, email) VALUES ('bruce', 'bruce@wayne.com')")
    connection.commit()
    print("Valid entry inserted into users table")
except sqlite3.IntegrityError as e:
    print("IntegrityError occurred for valid entry:", e)


try:
    cursor.execute("INSERT INTO users (username, email) VALUES (NULL, 'bsw@snyder.com')")  
    connection.commit()
except sqlite3.IntegrityError as e:
    print("Error occurred for NULL username:", e)

try:
    cursor.execute("INSERT INTO users (username, email) VALUES ('clark', NULL)") 
    connection.commit()
except sqlite3.IntegrityError as e:
    print("IntegrityError occurred for NULL email:", e)



connection.close()
