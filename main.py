from http.client import responses
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import mysql.connector
import json
import os

from config import config

from models.ModelUser import ModelUser
from models.entities.User import User
from model import Materia

# SB ADMIN boostrap
# Charisma
# orm flask

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(config['development'])
db = MySQL(app)
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
def users():
    columnas = "username, fullname"
    tabla = "users"
    orden = "username"
    col = ["Usuario", "Nombre y apellido"]
    response = get_tabla(columnas,col,tabla,orden)
    return render_template('table.html', title="Usuarios", data=response)


@app.route('/materias', methods=['GET', 'POST'])
def materias():
    columnas = "nombre"
    tabla = "materias"
    orden = "idmateria"
    col = ["Nombre"]
    response = get_tabla(columnas,col,tabla,orden)
    return render_template('table.html', title="Materias", data=response)

@app.route('/new_materias', methods=['GET', 'POST'])
def add_materias():
    if request.method == "POST":
        materia = Materia(0, request.form["nombre_mat"], request.form["descript_mat"])
        Materia.nuevo(db, materia)
        return redirect(url_for('materias'))
    else: 
        return render_template('/Tablas/materias.html', title="Materias")


def get_tabla(columnas,col,tabla,orden):
    cursor = db.connection.cursor()
    cursor.execute(f"SELECT {columnas} FROM {tabla} ORDER BY {orden} asc;")
    lista = cursor.fetchall()
    cursor.close()
    data = "[{"
    comilla = f"{chr (34)}"
    c = 1
    if lista:
        for row in lista:
            for i in range(0, len(lista[0])):
                data = data + comilla + str(col[i]) + comilla + ": "
                if type(row[i]) == str:
                    data = data + comilla + row[i] + comilla
                else:
                    data = data + str(row[i])
                if not i == (len(lista[0])-1):
                    data = data + ", "
            if c < (len(lista)):
                data = data + "}" + ", {"
            c+=1
        data = data + "}]"
    else:
        data = []
        for i in range(0, len(col[0])):
            data.append({
                f'{col[i]}': "",
            })
        a = str(str(data).replace("}, {", ", "))
        a = str(str(a).replace("'", f"{chr (34)}"))
        data = a
    response = {'data': json.loads(data),
                'tabla': f"{tabla}",}
    return response
    


def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    #flash("Parece que no iniciaste sesión...")
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
