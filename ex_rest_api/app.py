#!flask/bin/python

from flask import Flask, jsonify, abort
from flask import request
import pandas
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Here we can set the next part of a mini DB to construct the next manner as we can see
task = [
    {
        'id': 1,
        'title': u'Bay groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False

    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python Tutorial on the Web ',
        'done': False
    }
]


# Here we can instante the flask app as we can see
# Basically this is the manner to the app of calling the index subroutine
@app.route('/products', methods=['GET'])
def get_task():
    if len(task) == 0:
        abort(404)  # This is the basic error as we can note
    return jsonify({'task': task})  # Here we calling the jsonify as an output method


if __name__ == '__main__':
    app.run(debug=True)  # Here we can use the debug implicit manner
