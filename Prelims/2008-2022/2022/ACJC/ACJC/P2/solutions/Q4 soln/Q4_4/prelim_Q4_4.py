from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/choice')
def choice():
    if request.args['choice'] == '1':
        return render_template('insert.html')
    else:
        db = sqlite3.connect('Task4.db')
        data = db.execute('''SELECT books.bookID, books.title, copies.copyID, books.price
                          from books, copies WHERE books.bookID = copies.bookID
                          order by books.bookID asc''')
        dic = {}
        for item in data:
            if item[0] not in dic:
                dic[item[0]] = [item[1],item[3],1]
            else:
                dic[item[0]][2] += 1
                    
        return render_template('display.html', infor = dic)

@app.route('/insert')
def insert():
    data = request.args
    db = sqlite3.connect('Task4.db')
    db.execute('INSERT INTO books values (?,?,?)',
               (data['bookid'], data['title'], data['price']))
    for i in range(1,int(data['no_copies'])+1):
        copyid = "0"*(4-len(str(i))) + str(i)
        db.execute('INSERT INTO copies values (?,?)',
               (data['bookid'], copyid))
                   
    db.commit() 
    return "Success!"

app.run()

#create connection to task4.db
#SELECT books.bookID, books.title, copies.copyID, books.price
#from books, copies WHERE books.bookID = copies.bookID or books inner join copies on books.bookID = copies.bookID
#order by books.bookID asc
#method to count number of copies
#display results in html table

#browser view of results
#shows correct results
