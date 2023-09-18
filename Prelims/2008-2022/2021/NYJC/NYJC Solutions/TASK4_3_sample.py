# Task 4.3
# Date: 18/08/2021
# Author: Mr Ng
# Description: Code for Task 4.3
# Version: 1

import sqlite3
from flask import Flask, render_template, request

class Book:
    def __init__(self, id_, title, price, type_):
        self.id = id_
        self.title = title
        self.price = price
        self.type = type_
    
    def price(self):
        return self.price / 100

class Cart:
    def __init__(self):
        self.items = []

    def add(self, book):
        self.items.append(book)
    
    def total_price(self):
        # return sum of book prices
        total = 0
        for book in self.items:
            total += book.price
        return round(total, 2)

app = Flask(__name__)

bookcart = Cart()

conn = sqlite3.connect('bookstore.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM Book;''')
booklist = cur.fetchall()  # tuple: id, title, price
conn.close()

@app.route('/', methods=['GET'])
def cart():
    # If not GET argument, display page
    if 'bookid' in request.args:
        # If GET argument, add book then display page
        id_ = request.args['bookid']
        conn = sqlite3.connect('bookstore.db')
        cur = conn.cursor()
        cur.execute(
            '''SELECT * FROM Book WHERE BookID = ?;''',
            (id_,),
        )
        rec = cur.fetchone()  # tuple: id, title, price, type
        conn.close()
        book = Book(rec[0], rec[1], rec[2], rec[3])
        bookcart.add(book)
    return render_template(
        'cart.html',
        booklist=booklist,
        cart=bookcart,
    )

app.run()
