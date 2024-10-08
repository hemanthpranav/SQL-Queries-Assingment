import sqlite3
from tabulate import tabulate


connection = sqlite3.connect('foreignkey.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL
    
    )
''')


cursor.execute('''
    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY,
        book_title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
               )
''')



cursor.execute("INSERT INTO authors (author_name)  VALUES ('CLARK')")
cursor.execute("INSERT INTO authors (author_name) VALUES ('HEMANTH')")
cursor.execute("INSERT INTO authors (author_name) VALUES ('BRUCE')")

cursor.execute("INSERT INTO books (book_title, author_id) VALUES ('Superman', 1)")
cursor.execute("INSERT INTO books (book_title, author_id) VALUES ('Fountain', 2)")
cursor.execute("INSERT INTO books (book_title, author_id) VALUES ('Batman', 3)")
cursor.execute("INSERT INTO books (book_title, author_id) VALUES ('Lex luthor', 1)")

connection.commit()


query = '''
 SELECT 
        a.author_name, 
        b.book_title 
    FROM 
        authors a
    JOIN 
        books b ON a.author_id = b.author_id;
'''


cursor.execute(query)


foreign = cursor.fetchall()


headings = ['Author Name', 'Book Title']
final = foreign

print("\n Authors and books:")
print(tabulate(final, headers=headings, tablefmt='grid'))
connection.close()