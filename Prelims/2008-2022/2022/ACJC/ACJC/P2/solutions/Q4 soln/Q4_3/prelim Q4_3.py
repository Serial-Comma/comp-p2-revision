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
        return render_template('index.html')

@app.route('/insert')
def insert():
    data = request.args
    db = sqlite3.connect('Task4.db')
    db.execute('INSERT INTO books values (?,?,?)',
               (data['bookid'], data['title'], data['price']))
    for i in range(1,int(data['no_copies'])+1):
        copyid = "0"*(4-len(str(i))) + str(i)
        db.execute('INSERT INTO copies values (?,?)',
               (copyid,data['bookid'], ))
                   
    db.commit() 
    return "Success!"

app.run()

#create connection to task4.db
#html to receive inputs
#received form input
#successfully insert into books
#successfully insert into copies with correct copyID
#database committed

#database shows example successfully inserted
