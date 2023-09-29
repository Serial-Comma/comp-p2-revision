#Task 4.1
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/details')
def details():
    import sqlite3
    with sqlite3.connect("./FITNESS.db") as conn:
            details = conn.execute('''
    SELECT 
    Member.Name,
    Member.Gender,
    MAX(FitnessRecord.WorkoutDate)
    FROM Member
    LEFT JOIN FitnessRecord ON Member.MemberID = FitnessRecord.MemberID
    GROUP BY Name
    ORDER BY Gender ASC, Name ASC

    ''')
    lst = []
    # descriptions = ''
    # for description in details.description:
    #     descriptions +=f"{description[0]} "



    for row in details:
        lst.append(row)

    # lst.insert(0,descriptions)
    print(lst)


    return render_template("details.html",lst=lst)

app.run()