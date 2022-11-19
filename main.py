from http.client import responses
from tkinter import N
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from werkzeug.utils import secure_filename

from config import config

from models.ModelUser import ModelUser
from models.entities.User import User
from model import *
import base64

from static.funciones.funciones import *


# SB ADMIN boostrap
# Charisma
# orm flask

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(config['development'])
UPLOAD_FOLDER = 'D:/Downloads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
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
    return render_template('table.html', title="Usuarios", data=response)

@app.route('/materias', methods=['GET', 'POST'])
def materias():
    response = Materia.get_tabla(db)
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

@app.route('/secciones', methods=['GET', 'POST'])
def secciones():
    response = Secciones.get_tabla(db)
    return render_template('table.html', title="Secciones", data=response)

@app.route('/secciones/<id>', methods=['GET', 'POST'])
def ver_secciones(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            seccion = Secciones(id, request.form["Nombre"])
            Secciones.update(db, seccion)
        elif request.form["btn_submit"] == "btn_delete":
            Secciones.delete(db, id)
        return redirect(url_for('secciones'))
    else:
        data, permisos = Secciones.ver(db,id)
        return render_template('/Tablas/secciones.html', title="Secciones", data=data, permisos=permisos)

@app.route('/new_secciones', methods=['GET', 'POST'])
def add_secciones():
    if request.method == "POST":
        seccion = Secciones(0, request.form["Nombre"])
        Secciones.nuevo(db, seccion)
        return redirect(url_for('secciones'))
    else: 
        return render_template('/Tablas/secciones.html', title="Secciones", data="", permisos="")

@app.route('/nivel_escolar', methods=['GET', 'POST'])
def nivel_escolar():
    response = Nivel_escolar.get_tabla(db)
    return render_template('table.html', title="Nivel Escolar", data=response)

@app.route('/nivel_escolar/<id>', methods=['GET', 'POST'])
def ver_nivel_escolar(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            nivel = Nivel_escolar(id, request.form["Nombre_Exig"], request.form["Exig"])
            Nivel_escolar.update(db, nivel)
        elif request.form["btn_submit"] == "btn_delete":
            Nivel_escolar.delete(db, id)
        return redirect(url_for('nivel_escolar'))
    else:
        data, permisos = Nivel_escolar.ver(db,id)
        return render_template('/Tablas/nivel_escolar.html', title="Nivel escolar", data=data, permisos=permisos)

@app.route('/new_nivel_escolar', methods=['GET', 'POST'])
def add_nivel_escolar():
    if request.method == "POST":
        nivel = Nivel_escolar(0, request.form["Nombre_Exig"], request.form["Exig"])
        Nivel_escolar.nuevo(db, nivel)
        return redirect(url_for('nivel_escolar'))
    else: 
        return render_template('/Tablas/nivel_escolar.html', title="Nivel escolar", data="", permisos="")

@app.route('/tutores', methods=['GET', 'POST'])
def tutores():
    response = Tutor.get_tabla(db)
    return render_template('table.html', title="Tutores", data=response)

@app.route('/tutores/<id>', methods=['GET', 'POST'])
def ver_tutor(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            tutor = Tutor(id, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["email"], request.form["domicilio"])
            Tutor.update(db, tutor)
        elif request.form["btn_submit"] == "btn_delete":
            Tutor.delete(db, id)
        return redirect(url_for('tutores'))
    else:
        data, permisos = Tutor.ver(db,id)
        return render_template('/Tablas/tutores.html', title="Tutores", data=data, permisos=permisos)

@app.route('/new_tutores', methods=['GET', 'POST'])
def add_tutor():
    if request.method == "POST":
        tutor = Tutor(0, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["email"], request.form["domicilio"])
        Tutor.nuevo(db, tutor)
        return redirect(url_for('tutores'))
    else: 
        return render_template('/Tablas/tutores.html', title="Tutores", data="", permisos="")

@app.route('/gravedad', methods=['GET', 'POST'])
def gravedad():
    response = Gravedad.get_tabla(db)
    return render_template('table.html', title="Gravedad", data=response)

@app.route('/gravedad/<id>', methods=['GET', 'POST'])
def ver_gravedad(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            gravedad = Gravedad(id, request.form["nombre"], request.form["descript"])
            Gravedad.update(db, gravedad)
        elif request.form["btn_submit"] == "btn_delete":
            Gravedad.delete(db, id)
        return redirect(url_for('gravedad'))
    else:
        data, permisos = Gravedad.ver(db,id)
        return render_template('/Tablas/gravedad.html', title="Gravedad", data=data, permisos=permisos)

@app.route('/new_gravedad', methods=['GET', 'POST'])
def add_gravedad():
    if request.method == "POST":
        gravedad = Gravedad(0, request.form["nombre"], request.form["descript"])
        Gravedad.nuevo(db, gravedad)
        return redirect(url_for('gravedad'))
    else: 
        return render_template('/Tablas/gravedad.html', title="Gravedad", data="", permisos="")

@app.route('/tipo_procs', methods=['GET', 'POST'])
def tipo_procs():
    response = Tipo_procesos.get_tabla(db)
    return render_template('table.html', title="Tipo Procesos", data=response)

@app.route('/tipo_procesos/<id>', methods=['GET', 'POST'])
def ver_tipo_procs(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            tipo_proc = Tipo_procesos(id, request.form["nombre"])
            Tipo_procesos.update(db, tipo_proc)
        elif request.form["btn_submit"] == "btn_delete":
            Tipo_procesos.delete(db, id)
        return redirect(url_for('tipo_procs'))
    else:
        data, permisos = Tipo_procesos.ver(db,id)
        return render_template('/Tablas/tipo_procs.html', title="Tipo Procesos", data=data, permisos=permisos)

@app.route('/new_tipo_procesos', methods=['GET', 'POST'])
def add_tipo_procs():
    if request.method == "POST":
        tipo_proc = Tipo_procesos(0, request.form["nombre"])
        Tipo_procesos.nuevo(db, tipo_proc)
        return redirect(url_for('tipo_procs'))
    else: 
        return render_template('/Tablas/tipo_procs.html', title="Tipo Procesos", data="", permisos="")

@app.route('/visitantes', methods=['GET', 'POST'])
def visitantes():
    response = Visitante.get_tabla(db)
    return render_template('table.html', title="Visitantes", data=response)

@app.route('/visitantes/<id>', methods=['GET', 'POST'])
def ver_visitantes(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            visitante = Visitante(id, request.form["nombre"], request.form["apellido"], request.form["telefono"])
            Visitante.update(db, visitante)
        elif request.form["btn_submit"] == "btn_delete":
            Visitante.delete(db, id)
        return redirect(url_for('visitantes'))
    else:
        data, permisos = Visitante.ver(db,id)
        return render_template('/Tablas/visitantes.html', title="Visitantes", data=data, permisos=permisos)

@app.route('/new_visitantes', methods=['GET', 'POST'])
def add_visitantes():
    if request.method == "POST":
        visitante = Visitante(0, request.form["nombre"], request.form["apellido"], request.form["telefono"])
        Visitante.nuevo(db, visitante)
        return redirect(url_for('visitantes'))
    else: 
        return render_template('/Tablas/visitantes.html', title="Visitantes", data="", permisos="")

@app.route('/historial_de_ingresos', methods=['GET', 'POST'])
def his_de_ing():
    response = Historial_ingreso.get_tabla(db)
    return render_template('table.html', title="Historial de Ingresos", data=response)

@app.route('/historial_de_ingresos/<id>', methods=['GET', 'POST'])
def ver_his_de_ing(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            hist = Historial_ingreso(id, request.form["fecha"], request.form["descripcion"])
            vis_dia_raw = request.form.getlist("id_det")
            vis_dia = limpia_sub_tabla_uniq(vis_dia_raw)
            Historial_ingreso.update(db, hist, vis_dia)
        elif request.form["btn_submit"] == "btn_delete":
            Historial_ingreso.delete(db, id)
        return redirect(url_for('his_de_ing'))
    else:
        data, permisos, data_det = Historial_ingreso.ver(db,id)
        data_sec = Visitante.get_tabla(db)
        return render_template('/Tablas/his_de_ing.html', title="Historial de Ingresos", data=data, permisos=permisos, data_sec=data_sec, data_det=data_det)

@app.route('/new_historial_de_ingresos', methods=['GET', 'POST'])
def add_his_de_ing():
    if request.method == "POST":
        hist = Historial_ingreso(0, request.form["fecha"], request.form["descripcion"])
        vis_dia = request.form.getlist("id_det")
        Historial_ingreso.nuevo(db, hist, vis_dia)
        return redirect(url_for('his_de_ing'))
    else: 
        data = Visitante.get_tabla(db)
        return render_template('/Tablas/his_de_ing.html', title="Historial de Ingresos", data="", permisos="", data_sec=data)

@app.route('/indicadores', methods=['GET', 'POST'])
def indicadores():
    response = Indicadores.get_tabla(db)
    return render_template('table.html', title="Indicadores", data=response)

@app.route('/indicadores/<id>', methods=['GET', 'POST'])
def ver_indicadores(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            ind = Indicadores(0, request.form["descripcion"])
            Indicadores.update(db, ind)
        elif request.form["btn_submit"] == "btn_delete":
            Indicadores.delete(db, id)
        return redirect(url_for('indicadores'))
    else:
        data, permisos = Indicadores.ver(db,id)
        return render_template('/Tablas/indicadores.html', title="Indicadores", data=data, permisos=permisos)

@app.route('/new_indicadores', methods=['GET', 'POST'])
def add_indicadores():
    if request.method == "POST":
        ind = Indicadores(0, request.form["descripcion"])
        Indicadores.nuevo(db, ind)
        return redirect(url_for('indicadores'))
    else: 
        return render_template('/Tablas/indicadores.html', title="Indicadores", data="", permisos="")

@app.route('/profesores', methods=['GET', 'POST'])
def profesores():
    response = Profesores.get_tabla(db)
    return render_template('table.html', title="Profesores", data=response)

@app.route('/profesores/<id>', methods=['GET', 'POST'])
def ver_profesores(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            profesor = Profesores(id, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"],request.form["telefono"],
                          request.form["email"], request.form["domicilio"])
            legajo_ids = request.form.getlist("id_det")
            legajo_data = request.files.getlist('legaj')
            legajo = []
            for i in range(0,len(legajo_ids)):
                legajo.append([legajo_ids[i], legajo_data[i], id])
            legajo = limpia_sub_tabla_multi(legajo)
            legajo_raw = convierte_img_a_64_multi(legajo)
            Profesores.update(db, profesor, legajo_raw)
        elif request.form["btn_submit"] == "btn_delete":
            Profesores.delete(db, id)
        return redirect(url_for('profesores'))
    else:
        data, permisos, data_det = Profesores.ver(db,id)
        return render_template('/Tablas/profesores.html', title="Profesores", data=data, permisos=permisos, data_det=data_det)

@app.route('/new_profesores', methods=['GET', 'POST'])
def add_profesores():
    if request.method == "POST":
        profesor = Profesores(0, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["telefono"], request.form["email"], request.form["domicilio"])
        legajo = request.files.getlist('legaj')
        legajo_raw = convierte_img_a_64(legajo)
        Profesores.nuevo(db, profesor, legajo_raw)
        return redirect(url_for('profesores'))
    else: 
        return render_template('/Tablas/profesores.html', title="Profesores", data="", permisos="")

@app.route('/profesores/legajo/dowload/<value>', methods=['GET', 'POST'])
def descarga_legajo(value):
    return convierte_64_a_img(db,value)

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    #flash("Parece que no iniciaste sesión...")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
