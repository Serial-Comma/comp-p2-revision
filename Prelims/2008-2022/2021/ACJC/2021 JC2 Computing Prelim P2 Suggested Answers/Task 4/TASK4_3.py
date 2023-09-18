from flask import *
import sqlite3

# Set up Flask
app = Flask(__name__) 

# Set up a route to render the HTML form
@app.route("/")
def root():
    return render_template("form.html")

# Set up another route to render the display HTML document
@app.route("/result", methods=["POST"])
def result():
    # Retrieve input from the HTML form
    location = request.form["location"]
    allergies = request.form.getlist("allergy")

    # Connect to the SQL database
    connection = sqlite3.connect("bento_company.db")
    connection.row_factory = sqlite3.Row

    # SQL statement to extract data for the given location
    bentos = connection.execute('''
                                SELECT *
                                FROM Kiosk, KioskBento, BentoBox
                                WHERE Kiosk.KioskID = KioskBento.KioskID
                                AND KioskBento.BentoName = BentoBox.BentoName
                                AND Kiosk.Location = ?
                                ''', (location,)).fetchall()

    # Close the connection to the SQL database
    connection.close()
    
    result = []

    # Filter out bentos based on allergies
    for i in bentos:
        if ("egg" in allergies and i['ContainEgg'] == 1 or
            "nut" in allergies and i['ContainNut'] == 1 or
            "seafood" in allergies and i['ContainSeafood'] == 1):
            continue

        result.append([i['BentoName'], i['SellPrice']])        

    # Render the HTML document and pass result
    return render_template("result.html", result=result)

app.run()
