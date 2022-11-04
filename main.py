from http.client import responses
from tkinter import N
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os

from config import config

from models.ModelUser import ModelUser
from models.entities.User import User
from model import *

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
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    columnas = "id_user, username, fullname"
    tabla = "users"
    orden = "username"
    col = ["ID", "Usuario", "Nombre y apellido"]
    estado = ""
    response = get_tabla(db, columnas, col, tabla, orden, estado)
    #print(response)
    return render_template('table.html', title="Usuarios", data=response)

@app.route('/materias', methods=['GET', 'POST'])
def materias():
    columnas = "idmateria, nombre"
    tabla = "materias"
    orden = "idmateria"
    col = ["ID", "Nombre"]
    estado = "WHERE estado = 1"
    response = get_tabla(db, columnas, col, tabla, orden, estado)
    return render_template('table.html', title="Materias", data=response)

@app.route('/materias/<id>', methods=['GET', 'POST'])
def ver_materias(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            materia = Materia(id, request.form["nombre_mat"], request.form["descript_mat"])
            Materia.update(db, materia)
        elif request.form["btn_submit"] == "btn_delete":
            Materia.delete(db, id)
        return redirect(url_for('materias'))
    else:
        data, permisos = Materia.ver(db,id)
        return render_template('/Tablas/materias.html', title="Materias", data=data, permisos=permisos)

@app.route('/new_materias', methods=['GET', 'POST'])
def add_materias():
    if request.method == "POST":
        materia = Materia(0, request.form["nombre_mat"], request.form["descript_mat"])
        Materia.nuevo(db, materia)
        return redirect(url_for('materias'))
    else: 
        return render_template('/Tablas/materias.html', title="Materias", data="", permisos="")

@app.route('/nivel_escolar', methods=['GET', 'POST'])
def nivel_escolar():
    columnas = "idnivel_escolar, nombre, exigencia"
    tabla = "nivel_escolar"
    orden = "idnivel_escolar"
    col = ["ID", "Nombre", "Exigencia"]
    estado = ""
    response = get_tabla(db, columnas, col, tabla, orden, estado)
    return render_template('table.html', title="Nivel Escolar", data=response)

@app.route('/nivel_escolar/<id>', methods=['GET', 'POST'])
def ver_nivel_escolar(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            nivel = Nivel_escolar(id, request.form["Nombre_Exig"], request.form["Exig"])
            Nivel_escolar.update(db, nivel)
        return redirect(url_for('nivel_escolar'))
    else:
        data = Nivel_escolar.ver(db,id)
        return render_template('/Tablas/nivel_escolar.html', title="Nivel escolar", data=data)

@app.route('/new_nivel_escolar', methods=['GET', 'POST'])
def add_nivel_escolar():
    if request.method == "POST":
        nivel = Nivel_escolar(0, request.form["Nombre_Exig"], request.form["Exig"])
        Nivel_escolar.nuevo(db, nivel)
        return redirect(url_for('nivel_escolar'))
    else: 
        return render_template('/Tablas/nivel_escolar.html', title="Nivel escolar", data="")

@app.route('/tutores', methods=['GET', 'POST'])
def tutores():
    columnas = "idtutor, nombres, apellidos"
    tabla = "tutores"
    orden = "nombres"
    col = ["ID", "Nombre", "Apellido"]
    estado = "WHERE estado = 1"
    response = get_tabla(db, columnas, col, tabla, orden, estado)
    return render_template('table.html', title="Tutores", data=response)

@app.route('/tutores/<id>', methods=['GET', 'POST'])
def ver_tutor(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            tutor = Tutor(id, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["email"], request.form["domicilio"])
            Tutor.update(db, tutor)
        return redirect(url_for('tutores'))
    else:
        data = Tutor.ver(db,id)
        return render_template('/Tablas/tutores.html', title="Tutores", data=data)

@app.route('/new_tutores', methods=['GET', 'POST'])
def add_tutor():
    if request.method == "POST":
        tutor = Tutor(0, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["email"], request.form["domicilio"])
        Tutor.nuevo(db, tutor)
        return redirect(url_for('tutores'))
    else: 
        return render_template('/Tablas/tutores.html', title="Tutores", data="")

@app.route('/gravedad', methods=['GET', 'POST'])
def gravedad():
    columnas = "idgravedad, nombre"
    tabla = "gravedad"
    orden = "idgravedad"
    col = ["ID", "Nombre"]
    estado = ""
    response = get_tabla(db, columnas, col, tabla, orden, estado)
    return render_template('table.html', title="Gravedad", data=response)

@app.route('/gravedad/<id>', methods=['GET', 'POST'])
def ver_gravedad(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            gravedad = Gravedad(id, request.form["nombre"], request.form["descript"])
            Gravedad.update(db, gravedad)
        return redirect(url_for('gravedad'))
    else:
        data, eliminar = Gravedad.ver(db,id)
        #return render_template('/Tablas/gravedad.html', title="Gravedad", data=data, eliminar=1)
        return render_template('/Tablas/gravedad.html', title="Gravedad", data=data, eliminar=eliminar)

@app.route('/new_gravedad', methods=['GET', 'POST'])
def add_gravedad():
    if request.method == "POST":
        gravedad = Gravedad(0, request.form["nombre"], request.form["descript"])
        Gravedad.nuevo(db, gravedad)
        return redirect(url_for('gravedad'))
    else: 
        return render_template('/Tablas/gravedad.html', title="Gravedad", data="")

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    #flash("Parece que no iniciaste sesión...")
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
