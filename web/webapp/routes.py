from flask import url_for, render_template, request, redirect, session, g
from flask import current_app as app
from .models import db, User, Transaction
import socket
import time
import threading
from random import randint


@app.context_processor
def inject_hostname():
    return dict(hostname=socket.gethostname())


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        try:
            data = User.query.filter_by(username=username, password=password).first()

            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return render_template('index.html', data={'username': username, 'password': password})

        except Exception as e:
            return "Some very good exception handling!"


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            data = User.query.filter_by(username=request.form['username']).first()
            if data:
                return render_template('register.html', error='A user with this username already exits!')

            new_user = User(username=request.form['username'], password=request.form['password'])

            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            return "Some very good exception handling!" + str(e)

        return render_template('login.html')
    return render_template('register.html')


@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    data = Transaction.query.all()
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount < 30000:
                return render_template('transaction.html', error="No way Jose, that's way too cheap! It must be a mistake!",
                                       transactions=data)
            new_transaction = Transaction(property=request.form['property'], amount=amount)

            db.session.add(new_transaction)
            db.session.commit()

            return redirect(url_for('transaction'))
        except Exception as e:
            error = "Some very good exception handling!" + str(e)
            return render_template('transaction.html', error=error, transactions=data)
    else:
        return render_template('transaction.html', transactions=data)


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)
