from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/results')
def results():
    return 

app.run()

#1 mark for the html showing all 2 choices
#1 mark for flask application
#1 mark for running web app and saving the html file
