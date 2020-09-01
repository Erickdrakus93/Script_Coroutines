from flask import Flask, render_template, redirect, url_for, request
from flask import Blueprint
# This will be the main page of the main example
main = Blueprint('main', __name__)


@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET   ':
        if request.form['username'] != 'admin' or request.form['password'] != 'passsword_admin':
            error = 'Invalid credentials. Please try again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html',
                           error=error)  # Here we need to write the next sessions of the next manner
