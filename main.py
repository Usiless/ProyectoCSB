#from crypt import methods
from flask import Flask, session, render_template, request, redirect, g, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
picFolder 



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == '12':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
    return render_template('login.html')


@app.route('/protected')
def protected():
    if g.user:
        return render_template('index.html', user=session['user'])
    return redirect(url_for('login'))


@app.route('/about/')
def about():
    return render_template('about.html')


@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)
