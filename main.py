﻿from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import mysql.connector
import json
import os

from config import config

from models.ModelUser import ModelUser
from models.ModelUser import ModelUser
from models.entities.User import User
# SB ADMIN boostrap
# Charisma
# orm flask

app = Flask(__name__)
app.secret_key = os.urandom(24)
db = MySQL(app)
mydb = mysql.connector.connect(    
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'csb_prov')
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def start():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
                return render_template('login.html')
        else:
            flash("Usuario no encontrando")
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/home')
@login_required
def home():
    return render_template('index.html')


@app.route('/about')
@login_required
def about():
    return render_template('about.html')


@app.route('/news')
@login_required
def news():
    return render_template('news.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/users', methods=['GET', 'POST'])
def profesores():
    columnas = "username, fullname"
    tabla = "users"
    orden = "username"
    col = ["Usuario", "Nombre y apellido"]
    lista = get_tabla(columnas,col,tabla,orden)
    data = []
    for row in lista:
        data.append({
            f'{col[0]}': row[0],
            f'{col[1]}': row[1],
            })
    response = {'data': data,}
    return render_template('table.html', title="Usuarios", data=response)


def get_tabla(columnas,col,tabla,orden):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT {columnas} FROM {tabla} ORDER BY {orden} asc;")
    lista = cursor.fetchall()
    cursor.close()
    return lista
    


def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    #flash("Parece que no iniciaste sesión...")
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()