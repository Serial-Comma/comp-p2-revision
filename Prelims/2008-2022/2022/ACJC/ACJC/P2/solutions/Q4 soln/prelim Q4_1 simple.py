import sqlite3
f1 = open('books_data.txt')
f2 = open('copies_data.txt')
books = []
copies = []

for line in f1:
    book = line.strip().split(',')
    books.append(book)
    
for line in f2:
    copy = line.strip().split(',')
    copies.append(copy)

print(books)
print(copies)

db = sqlite3.connect('Task4 - simple.db')

#inserting into books
for item in books:
    db.execute('INSERT INTO books values(?,?,?)', (item[0],item[1],item[2]))

#inserting into copies
for item in copies:
    db.execute('INSERT INTO copies values(?,?)', (item[0],item[1]))

db.commit()
f1.close()
f2.close()

#connection to database
#correct insertion of data into books table
#correct insertion of data into copies table
#database transaction committed
               
