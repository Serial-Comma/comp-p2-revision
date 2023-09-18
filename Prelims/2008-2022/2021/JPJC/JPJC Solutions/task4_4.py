from task4 import *
import flask

app = flask.Flask(__name__, template_folder="TASK4_4")

@app.route('/')
def start():
    return flask.render_template('start.html')

@app.route('/display/')
def display():
    if 'brand' in flask.request.args:
        value = flask.request.args['brand']
        rows = []
        result = coll.find()
        for doc in result:
            if doc.get('brand') == 'solo':
                rows.append((doc.get('price'),doc.get('model'),doc.get('colour')))
        for i in range(len(rows)):
            for j in range(len(rows)-i-1):
                if rows[j]>rows[j+1]:
                    rows[j],rows[j+1] = rows[j+1],rows[j]
        
        return flask.render_template('display.html',brand=value,rows=rows)

if __name__ == '__main__':
    app.run()
