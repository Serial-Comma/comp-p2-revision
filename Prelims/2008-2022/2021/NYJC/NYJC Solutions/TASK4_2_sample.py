# Task 4.2
# Date: 18/08/2021
# Author: Mr Ng
# Description: Code for Task 4.2
# Version: 1

import csv, sqlite3

class Book:
    def __init__(self, title, price, type_):
        self.title = title
        self.price = price
        self.type = type_

class PrintedBook(Book):
    def __init__(self, title, price, weight):
        self.title = title
        self.price = price
        self.weight = weight

class VirtualBook(Book):
    def __init__(self, title, price, download_link):
        self.title = title
        self.price = price
        self.download_link = download_link
        
class Cart:
    def __init__(self):
        self.items = []
    
    def total_price(self):
        '''
        Returns sum of all book.price in the cart.
        '''
        total = 0
        for book in self.items:
            total += book.price
        return total

conn = sqlite3.connect('bookstore.db')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Book;''')
cur.execute('''DROP TABLE IF EXISTS Printed;''')
cur.execute('''DROP TABLE IF EXISTS Virtual;''')
cur.execute(
    '''CREATE TABLE Book (
    BookID INTEGER,
    Title TEXT,
    Price INTEGER,
    Type TEXT CHECK(Type = 'Physical' OR Type = 'Virtual'),
    PRIMARY KEY (BookID)
);
''')
cur.execute(
    '''CREATE TABLE Printed (
    BookID INTEGER,
    Weight INTEGER,
    PRIMARY KEY (BookID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);
''')
cur.execute(
    '''CREATE TABLE Virtual (
    BookID INTEGER,
    DownloadLink TEXT,
    PRIMARY KEY (BookID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);
''')
conn.commit()
conn.close()

with open('bookstore.txt', 'r') as f:
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    for row in csv.reader(f):
        title, price, type_, weight, download_link = row  # list unpacking
        price = int(price.replace('.', ''))
        if type_ == 'Physical':
            book = PrintedBook(title, price, type_, weight)
        elif type_ == 'Virtual':
            book = VirtualBook(title, price, type_, download_link)
        cur.execute('''
            INSERT INTO Book (Title,Price,Type) VALUES (?, ?, ?)
        ''',
            (book.title, book.price, book.type)
        )
        cur.execute('''
        SELECT * FROM Book
        WHERE Title = ?;
        ''',
        (book.title,)
        )
        id_ = cur.fetchone()[0]
        if type_ == 'Physical':
            cur.execute('''
                INSERT INTO Printed VALUES (?, ?)
            ''',
            (id_, book.weight)
            )
        elif type_ == 'Virtual':
            cur.execute('''
                INSERT INTO Virtual VALUES (?, ?)
            ''',
            (id_, book.download_link)
            )
    conn.commit()
    conn.close()
        
