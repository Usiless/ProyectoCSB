from asyncio.windows_events import NULL
from flask import abort, Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from functools import wraps
from datetime import date

from config import config

from models.ModelUser import ModelUser
from models.entities.User import User
from model import *

from static.funciones.funciones import *
from static.funciones.funciones_plani import planilla_proc_detallado, planilla_proc_grado

# SB ADMIN boostrap
# Charisma
# orm flask

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(config['development'])
UPLOAD_FOLDER = 'planillas'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
db = MySQL(app)
login_manager_app = LoginManager(app)
app.jinja_env.filters['zip'] = zip

from datetime import datetime

#------------------LOGINS---------------------#

def role_required(roles):
    def decorator(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            rol = session["rol"]
            if app.config.get("LOGIN_DISABLED"):
                pass
            elif not rol in roles:
                abort(403)
            return func(*args, **kwargs)

        return decorated_view
    return decorator

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def start():
    return redirect(url_for('noticias'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                session["rol"] = logged_user.rol
                obtener_permisos_menu(db)
                return redirect(url_for('noticias'))
            else:
                flash("Contraseña incorrecta")
                return render_template('login.html')
        else:
            flash("Usuario no encontrando")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('noticias'))

#------------------USERS---------------------#

@app.route('/users', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def users():
    response = User_local.ver_users(db)
    return render_template('table.html', title="Usuarios", data=response)

@app.route('/users/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def ver_users(id):
    if request.method == "POST":
        User_local.update_rol(db,id,request.form["rol"])
        return redirect(url_for('users'))
    else:
        user = ModelUser.get_by_id(db,id)
        response = user.username, user.fullname, user.email, user.rol
        permisos = session["permisos"]["users"]
        roles = get_tabla_raw(db, "idtipo_user, nombre","tipo_user",0)
        return render_template('/Tablas/user_para_admin.html', title="Usuarios", data=response, data_sec=roles, permisos=permisos)

@app.route('/new_users', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def add_users():
    if request.method == "POST":
        User_local.nuevo(db,request.form["username"],request.form["realname"],request.form["email"],request.form["rol"])
        return redirect(url_for('users'))
    else:
        roles = get_tabla_raw(db, "idtipo_user, nombre","tipo_user",0)
        return render_template('/Tablas/user_para_admin.html', title="Usuarios", data="", permisos="", data_sec=roles)

#------------------ACERCA DE---------------------#

@app.route('/about')
def about():
    return render_template('about.html', title="Horarios de Clase")

#------------------MATERIAS---------------------#

@app.route('/materias', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo','profesor'])
def materias():
    response = Materia.get_tabla(db)
    return render_template('table.html', title="Materias", data=response)

@app.route('/materias/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo','profesor'])
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
@login_required
@role_required(['admin','directivo'])
def add_materias():
    if request.method == "POST":
        materia = Materia(0, request.form["nombre_mat"], request.form["descript_mat"])
        Materia.nuevo(db, materia)
        return redirect(url_for('materias'))
    else: 
        return render_template('/Tablas/materias.html', title="Materias", data="", permisos="")

#------------------SECCIONES---------------------#

@app.route('/secciones', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def secciones():
    response = Secciones.get_tabla(db)
    return render_template('table.html', title="Secciones", data=response)

@app.route('/secciones/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
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
@login_required
@role_required(['admin','directivo'])
def add_secciones():
    if request.method == "POST":
        seccion = Secciones(0, request.form["Nombre"])
        Secciones.nuevo(db, seccion)
        return redirect(url_for('secciones'))
    else: 
        return render_template('/Tablas/secciones.html', title="Secciones", data="", permisos="")

#------------------NIVEL ESCOLAR---------------------#

@app.route('/nivel_escolar', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def nivel_escolar():
    response = Nivel_escolar.get_tabla(db)
    return render_template('table.html', title="Nivel Escolar", data=response)

@app.route('/nivel_escolar/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
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
@login_required
@role_required(['admin','directivo'])
def add_nivel_escolar():
    if request.method == "POST":
        nivel = Nivel_escolar(0, request.form["Nombre_Exig"], request.form["Exig"])
        Nivel_escolar.nuevo(db, nivel)
        return redirect(url_for('nivel_escolar'))
    else: 
        return render_template('/Tablas/nivel_escolar.html', title="Nivel escolar", data="", permisos="")

#------------------TUTORES---------------------#

@app.route('/tutores', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def tutores():
    response = Tutor.get_tabla(db)
    return render_template('table.html', title="Tutores", data=response)

@app.route('/tutores/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
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
@login_required
@role_required(['admin','directivo', 'profesor'])
def add_tutor():
    if request.method == "POST":
        tutor = Tutor(0, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["email"], request.form["domicilio"])
        Tutor.nuevo(db, tutor)
        return redirect(url_for('tutores'))
    else: 
        return render_template('/Tablas/tutores.html', title="Tutores", data="", permisos="")

#------------------GRAVEDADES(observaciones)---------------------#

@app.route('/gravedad', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def gravedad():
    response = Gravedad.get_tabla(db)
    return render_template('table.html', title="Gravedad", data=response)

@app.route('/gravedad/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
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
@login_required
@role_required(['admin','directivo'])
def add_gravedad():
    if request.method == "POST":
        gravedad = Gravedad(0, request.form["nombre"], request.form["descript"])
        Gravedad.nuevo(db, gravedad)
        return redirect(url_for('gravedad'))
    else: 
        return render_template('/Tablas/gravedad.html', title="Gravedad", data="", permisos="")

#------------------TIPO DE PROCESOS---------------------#

@app.route('/tipo_procs', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def tipo_procs():
    response = Tipo_procesos.get_tabla(db)
    return render_template('table.html', title="Tipo Procesos", data=response)

@app.route('/tipo_procesos/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
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
@login_required
@role_required(['admin','directivo', 'profesor'])
def add_tipo_procs():
    if request.method == "POST":
        tipo_proc = Tipo_procesos(0, request.form["nombre"])
        Tipo_procesos.nuevo(db, tipo_proc)
        return redirect(url_for('tipo_procs'))
    else: 
        return render_template('/Tablas/tipo_procs.html', title="Tipo Procesos", data="", permisos="")

#------------------VISISTANTES---------------------#

@app.route('/visitantes', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero'])
def visitantes():
    response = Visitante.get_tabla(db)
    return render_template('table.html', title="Visitantes", data=response)

@app.route('/visitantes/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero'])
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
@login_required
@role_required(['admin','directivo', 'portero'])
def add_visitantes():
    if request.method == "POST":
        visitante = Visitante(0, request.form["nombre"], request.form["apellido"], request.form["telefono"])
        Visitante.nuevo(db, visitante)
        return redirect(url_for('visitantes'))
    else: 
        return render_template('/Tablas/visitantes.html', title="Visitantes", data="", permisos="")

#------------------HISTORIAL DE INGRESOS---------------------#

@app.route('/historial_de_ingresos', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero', 'personal', 'profesor'])
def his_de_ing():
    response = Historial_ingreso.get_tabla(db)
    return render_template('table.html', title="Historial de Ingresos", data=response)

@app.route('/historial_de_ingresos/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero', 'personal', 'profesor'])
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
@login_required
@role_required(['admin','directivo', 'portero'])
def add_his_de_ing():
    if request.method == "POST":
        hist = Historial_ingreso(0, request.form["fecha"], request.form["descripcion"])
        vis_dia = request.form.getlist("id_det")
        Historial_ingreso.nuevo(db, hist, vis_dia)
        return redirect(url_for('his_de_ing'))
    else: 
        data = Visitante.get_tabla(db)
        return render_template('/Tablas/his_de_ing.html', title="Historial de Ingresos", data="", permisos="", data_sec=data)

#------------------INDICADORES---------------------#

@app.route('/indicadores', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def indicadores():
    response = Indicadores.get_tabla(db)
    return render_template('table.html', title="Indicadores", data=response)

@app.route('/indicadores/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def ver_indicadores(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            ind = Indicadores(id, request.form["descripcion"])
            Indicadores.update(db, ind)
        elif request.form["btn_submit"] == "btn_delete":
            Indicadores.delete(db, id)
        return redirect(url_for('indicadores'))
    else:
        data, permisos = Indicadores.ver(db,id)
        return render_template('/Tablas/indicadores.html', title="Indicadores", data=data, permisos=permisos)

@app.route('/new_indicadores', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def add_indicadores():
    if request.method == "POST":
        ind = Indicadores(0, request.form["descripcion"])
        Indicadores.nuevo(db, ind)
        return redirect(url_for('indicadores'))
    else: 
        return render_template('/Tablas/indicadores.html', title="Indicadores", data="", permisos="")

#------------------PROFESORES---------------------#

@app.route('/profesores', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor','alumnos'])
def profesores():
    response = Profesores.get_tabla(db)
    return render_template('table.html', title="Profesores", data=response)

@app.route('/profesores/<id>', methods=['GET', 'POST']) #Falta el update
@login_required
@role_required(['admin','directivo', 'profesor'])
def ver_profesores(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            profesor = Profesores(id, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"],request.form["telefono"],
                          request.form["email"], request.form["domicilio"])
            legajo_ids = request.form.getlist("id_det_leg")
            legajo_data = request.files.getlist('legaj')

            nuevo_grad_mat = set(zip(request.form.getlist('estado_nuevo'), request.form.getlist('grados'),request.form.getlist('materias')))

            estados = request.form.getlist('estado')

            legajo = []
            for i in range(0,len(legajo_ids)):
                legajo.append([legajo_ids[i], legajo_data[i], id])
            legajo = limpia_sub_tabla_multi_arch(legajo)
            legajo_raw = convierte_img_a_64_multi(legajo)

            Profesores.update(db, profesor, legajo_raw, limpia_sub_tabla_uniq(legajo_ids), estados, nuevo_grad_mat)

        elif request.form["btn_submit"] == "btn_delete":
            Profesores.delete(db, id)
        return redirect(url_for('profesores'))
    else:
        data, permisos, data_det, data_det_2 = Profesores.ver(db,id)
        grados = Grados.get_tabla_raw(db)
        materias = Materia.get_tabla_raw(db)
        return render_template('/Tablas/profesores.html', title="Profesores", data=data, permisos=permisos, data_det=data_det, data_det_2 = data_det_2, data_sec = grados, data_sec_2 = materias)

@app.route('/new_profesores', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def add_profesores():
    if request.method == "POST":
        profesor = Profesores(0, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["telefono"], request.form["email"], request.form["domicilio"])
        legajo = request.files.getlist('legaj')
        legajo_raw = convierte_img_a_64(legajo)
        grados = limpia_sub_tabla_uniq(request.form.getlist("grados"))
        materias = limpia_sub_tabla_uniq(request.form.getlist("materias"))
        estados = limpia_sub_tabla_uniq(request.form.getlist("estado_nuevo"))
        mat_grad_prof = []
        mat_grad_prof = combina_varios(grados, estados, materias)
        nuevo_grad_mat = set(zip(request.form.getlist('estado_nuevo'), request.form.getlist('grados'),request.form.getlist('materias')))
        print(nuevo_grad_mat)

        Profesores.nuevo(db, profesor, legajo_raw, nuevo_grad_mat)
        return redirect(url_for('profesores'))
    else: 
        grados = Grados.get_tabla_raw(db)
        materias = Materia.get_tabla_raw(db)
        return render_template('/Tablas/profesores.html', title="Profesores", data="", permisos="", data_sec = grados, data_sec_2 = materias)

#------------------GRADOS---------------------#

@app.route('/grados', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo','profesor'])
def grados():
    response = Grados.get_tabla(db)
    return render_template('table.html', title="Grados", data=response)

@app.route('/grados/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def ver_grados(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            data = Grados(id, request.form["grado"], request.form["seccion"], request.form["nivel"])
            Grados.update(db, data)
        elif request.form["btn_submit"] == "btn_delete":
            Grados.delete(db, id)
        return redirect(url_for('grados'))
    else:
        data, permisos = Grados.ver(db,id)
        data_sec = Secciones.get_tabla_raw(db)
        data_sec_2 = Nivel_escolar.get_tabla_raw(db)
        return render_template('/Tablas/grados.html', title="Grados", data=data, permisos=permisos, data_sec = data_sec, data_sec_2 = data_sec_2)

@app.route('/new_grados', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def add_grados():
    if request.method == "POST":
        data = Grados(0, request.form["grado"], request.form["seccion"], request.form["nivel"])
        Grados.nuevo(db, data)
        return redirect(url_for('grados'))
    else: 
        data_sec = Secciones.get_tabla_raw(db)
        data_sec_2 = Nivel_escolar.get_tabla_raw(db)
        return render_template('/Tablas/grados.html', title="Grados", data="", permisos="", data_sec = data_sec, data_sec_2 = data_sec_2)

#------------------HORARIO DE CLASES---------------------#

@app.route('/horario_all/', methods=['GET', 'POST'])
def horario():
    anho = date.today()
    anho = anho.year
    if request.method == "POST":
        anho = request.form["anho"]
    grados = Grados.get_tabla_raw(db)
    response = Horario.get_tabla(db, anho)

    return render_template('/Tablas/horarios_tabla.html', title="Horarios", data=response, grados=grados)

#@login_required
#@app.route('/horario/<id>', methods=['GET', 'POST']) #No se si inlcuir esta parte, depende del tipo de user a donde le lleva el link
#def ver_horario(id):
#    if request.method == "POST":
#        if request.form["btn_submit"] == "btn_editar":
#            data = Grados(id, request.form["grado"], request.form["seccion"], request.form["nivel"])
#            Grados.update(db, data)
#        elif request.form["btn_submit"] == "btn_delete":
#            Grados.delete(db, id)
#        return redirect(url_for('grados'))
#    else:
#        data, permisos = Grados.ver(db,id)
#        data_sec = Secciones.get_tabla_raw(db)
#        data_sec_2 = Nivel_escolar.get_tabla_raw(db)
#        return render_template('/Tablas/grados.html', title="Grados", data=data, permisos=permisos, data_sec = data_sec, data_sec_2 = data_sec_2)

#@login_required
#@app.route('/new_horario', methods=['GET', 'POST'])#Solo por Excel
#def add_horario():
#    if request.method == "POST":
#        data = Grados(0, request.form["grado"], request.form["seccion"], request.form["nivel"])
#        Grados.nuevo(db, data)
#        return redirect(url_for('grados'))
#    else: 
#        data_sec = Secciones.get_tabla_raw(db)
#        data_sec_2 = Nivel_escolar.get_tabla_raw(db)
#        return render_template('/Tablas/grados.html', title="Grados", data="", permisos="", data_sec = data_sec, data_sec_2 = data_sec_2)

#------------------DOCTORES---------------------#

@app.route('/doctores', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def doctores():
    response = Doctores.get_tabla(db)
    return render_template('table.html', title="Doctores", data=response)

@app.route('/doctores/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def ver_doctor(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            doctor = Doctores(id, request.form["nombre"], request.form["apellido"], request.form["reg_prof"])
            Doctores.update(db, doctor)
        elif request.form["btn_submit"] == "btn_delete":
            Doctores.delete(db, id)
        return redirect(url_for('doctores'))
    else:
        data, permisos = Doctores.ver(db,id)
        return render_template('/Tablas/doctores.html', title="Doctores", data=data, permisos=permisos)

@app.route('/new_doctores', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def add_doctor():
    if request.method == "POST":
        doctor = Doctores(id, request.form["nombre"], request.form["apellido"], request.form["reg_prof"])
        Doctores.nuevo(db, doctor)
        return redirect(url_for('doctores'))
    else: 
        return render_template('/Tablas/doctores.html', title="doctores", data="", permisos="")

#------------------AFECCIONES---------------------#

@app.route('/afecciones', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def afecciones():
    response = Afecciones.get_tabla(db)
    return render_template('table.html', title="Afecciones", data=response)

@app.route('/afecciones/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def ver_afecciones(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            seccion = Afecciones(id, request.form["descripcion"])
            Afecciones.update(db, seccion)
        elif request.form["btn_submit"] == "btn_delete":
            Afecciones.delete(db, id)
        return redirect(url_for('afecciones'))
    else:
        data, permisos = Afecciones.ver(db,id)
        return render_template('/Tablas/afecciones.html', title="Afecciones", data=data, permisos=permisos)

@app.route('/new_afecciones', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def add_afecciones():
    if request.method == "POST":
        afeccion = Afecciones(0, request.form["descripcion"])
        Afecciones.nuevo(db, afeccion)
        return redirect(url_for('afecciones'))
    else: 
        return render_template('/Tablas/afecciones.html', title="Afecciones", data="", permisos="")

#------------------ALUMNOS---------------------#

@app.route('/alumnos', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo','profesores','alumnos'])
def alumnos():
    response = Alumnos.get_tabla(db)
    return render_template('table.html', title="Alumnos", data=response)

@app.route('/alumnos/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo','profesores'])
def ver_alumnos(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            alumno = Alumnos(id, request.form["nombre"], request.form["apellido"], request.form["documento"], request.form["celular"], 
                                request.form["email"], request.form["grado"], request.form["fecha_nac"])
        
            alumnos_tutores = request.form.getlist('id_det_tut')

            alumnos_ficha = Ficha(0, request.form["fecha"], request.form["apt"], request.form["doctor"])
            ficha_det = set(zip(request.form.getlist('affection'),request.form.getlist('recomm')))
            Alumnos.update(db, alumno, alumnos_tutores, alumnos_ficha, ficha_det)

        elif request.form["btn_submit"] == "btn_delete":
            Alumnos.delete(db, id)
        return redirect(url_for('alumnos'))
    else:
        data, permisos, data_det, data_det_2= Alumnos.ver(db,id)
        tutores = Tutor.get_tabla(db)
        grados = Grados.get_tabla_raw(db)
        doctores = Doctores.get_tabla_raw(db)
        afecciones = Afecciones.get_tabla_raw(db)
        return render_template('/Tablas/alumnos.html', title="Alumnos", data=data, permisos=permisos, 
                               data_det=data_det, data_det_2 = data_det_2,
                               data_sec = tutores, data_sec_2 = grados, data_sec_3 = doctores, data_sec_4 = afecciones)

@app.route('/new_alumnos', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def add_alumnos():
    if request.method == "POST":
        alumno = Alumnos(0, request.form["nombre"], request.form["apellido"], request.form["documento"], request.form["celular"], 
                         request.form["email"], request.form["grado"], request.form["fecha_nac"])
        
        alumnos_tutores = request.form.getlist('id_det_tut')

        alumnos_ficha = Ficha(0,request.form["fecha"], request.form["apt"], request.form["doctor"])
        ficha_det = set(zip(request.form.getlist('affection'),request.form.getlist('recomm')))

        Alumnos.nuevo(db, alumno, alumnos_tutores, alumnos_ficha, ficha_det)
        return redirect(url_for('alumnos'))
    else: 
        tutores = Tutor.get_tabla(db)
        grados = Grados.get_tabla_raw(db)
        doctores = Doctores.get_tabla_raw(db)
        afecciones = Afecciones.get_tabla_raw(db)
        print(grados)
        return render_template('/Tablas/alumnos.html', title="Alumnos", data="", permisos="", 
                               data_det="", data_det_2 = "",
                               data_sec = tutores, data_sec_2 = grados, data_sec_3 = doctores, data_sec_4 = afecciones)

#------------------FICHAS MÉDICAS---------------------#

@app.route('/fichas_med/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo','profesores'])
def ver_ficha(id):
    if request.method == "POST":
        id_alumno = request.form["id_alum"]
        if request.form["btn_submit"] == "btn_editar":
            ficha = Ficha(id, request.form["fecha"], request.form["apt"], request.form["doctor"], id_alumno)
            ficha_det = set(zip(request.form.getlist('affection'),request.form.getlist('recomm')))
            Ficha.update(db, ficha, ficha_det)

        elif request.form["btn_submit"] == "btn_delete":
            Ficha.delete(db, id)

        return redirect(url_for('ver_alumnos',id=id_alumno))

    else:
        data, permisos, data_det = Ficha.ver(db,id)
        doctores = Doctores.get_tabla_raw(db)
        afecciones = Afecciones.get_tabla_raw(db)
        return render_template('/Tablas/ficha_med.html', title="Ficha Médica", data=data, permisos=permisos, 
                               data_det=data_det, data_sec = doctores, data_sec_2 = afecciones)

#------------------Historial Observaciones---------------------#

@app.route('/historial_observaciones', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero', 'personal', 'profesor'])
def hist_obs():
    response = Historial_obs.get_tabla(db)
    return render_template('table.html', title="Historial de Observaciones", data=response)

@app.route('/historial_observaciones/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero', 'personal', 'profesor'])
def ver_hist_obs(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            hist = Historial_obs(id, request.form["fecha"], request.form["descripcion"])
            obs_det = set(zip(request.form.getlist('id_det'), request.form.getlist('gravedad'),request.form.getlist('descrip_det')))
            Historial_obs.update(db, hist, obs_det)
        elif request.form["btn_submit"] == "btn_delete":
            Historial_obs.delete(db, id)
        return redirect(url_for('hist_obs'))
    else:
        data, permisos, data_det = Historial_obs.ver(db,id)
        data_sec = Alumnos.get_tabla(db)
        data_sec_2 = Gravedad.get_tabla_raw(db)
        return render_template('/Tablas/his_obs.html', title="Historial de Observaciones", data=data, permisos=permisos, data_det=data_det, data_sec=data_sec, data_sec_2=data_sec_2)

@app.route('/new_historial_observaciones', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero'])
def add_hist_obs():
    if request.method == "POST":
        hist = Historial_obs(0, request.form["fecha"], request.form["descripcion"])
        obs_det = set(zip(request.form.getlist('id_det'), request.form.getlist('gravedad'),request.form.getlist('descrip_det')))
        Historial_obs.nuevo(db, hist, obs_det)
        return redirect(url_for('hist_obs'))
    else: 
        data_sec = Alumnos.get_tabla(db)
        data_sec_2 = Gravedad.get_tabla_raw(db)
        return render_template('/Tablas/his_obs.html', title="Historial de Observaciones", data="", permisos="", data_sec=data_sec, data_sec_2=data_sec_2)


#------------------NOTICIAS---------------------#

@app.route('/noticias', methods=['GET', 'POST'])
def noticias():
    obtener_permisos_menu(db)
    response, permisos = Noticias.get_tabla_raw(db)
    cant = len(response)-1
    return render_template('news.html', title="Noticias", data=response, permisos = permisos, cant = cant)

@app.route('/noticias/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def edit_noticias(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            data = Noticias(id, request.form["fecha"], request.form["titulo"], request.form["encabezado"], 
                            request.form["descripcion"], request.form['username'],session["_user_id"])
            Noticias.update(db, data)
        elif request.form["btn_submit"] == "btn_delete":
            Noticias.delete(db, id)
        return redirect(url_for('noticias'))
    else:
        data, permisos = Noticias.ver(db,id)
        return render_template('/Tablas/noticias.html', title="Noticias", data=data, permisos=permisos)

@app.route('/noticia/<id>', methods=['GET'])
def ver_noticias(id):
    data, permisos = Noticias.ver(db,id)
    return render_template('/Tablas/noticias_view.html', title="Noticias", data=data, permisos=permisos)

@app.route('/new_noticias', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo'])
def add_noticias():
    if request.method == "POST":
        data = Noticias(0, request.form["fecha"], request.form["titulo"], request.form["encabezado"], request.form["descripcion"],request.form['username'],session["_user_id"])
        Noticias.nuevo(db, data)
        return redirect(url_for('noticias'))
    else: 
        return render_template('/Tablas/noticias.html', title="Noticias", data="", permisos="")

#------------------PERSONAL---------------------#

@app.route('/personal', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def personal():
    response = Personal.get_tabla(db)
    return render_template('table.html', title="Personal", data=response)

@app.route('/personal/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def ver_personal(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            personal = Personal(id, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["email"])
            Personal.update(db, personal)
        elif request.form["btn_submit"] == "btn_delete":
            Personal.delete(db, id)
        return redirect(url_for('personal'))
    else:
        data, permisos = Personal.ver(db,id)
        return render_template('/Tablas/personal.html', title="Personal", data=data, permisos=permisos)

@app.route('/new_personal', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def add_personal():
    if request.method == "POST":
        personal = Personal(0, request.form["nombre"], request.form["apellido"], 
                          request.form["documento"], request.form["celular"], 
                          request.form["email"])
        Personal.nuevo(db, personal)
        return redirect(url_for('personal'))
    else: 
        return render_template('/Tablas/personal.html', title="Personal", data="", permisos="")

#------------------ROLES---------------------#

@app.route('/tipo_user', methods=['GET', 'POST'])
@login_required
@role_required(['admin'])
def tipo_user():
    response = Rol.get_tabla(db)
    return render_template('table.html', title="Roles", data=response)

@app.route('/tipo_user/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin'])
def ver_tipo_user(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            rol = Rol(id, request.form["nombre"], request.form["descripcion"])
            det_raw = set(zip(request.form.getlist('id_tabla'), request.form.getlist('crear'),request.form.getlist('leer'),request.form.getlist('modificar'),request.form.getlist('eliminar')))
            Rol.update(db, rol, det_raw)
        elif request.form["btn_submit"] == "btn_delete":
            Rol.delete(db, id)
        return redirect(url_for('tipo_user'))
    else:
        data, data_det, permisos = Rol.ver(db,id)
        return render_template('/Tablas/roles.html', title="Roles", data=data, permisos=permisos, data_det=data_det)

@app.route('/new_tipo_user', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'portero'])
def add_tipo_user():
    if request.method == "POST":
        rol = Rol(0, request.form["nombre"], request.form["descripcion"])
        det_raw = set(zip(request.form.getlist('id_tabla'), request.form.getlist('crear'),request.form.getlist('leer'),request.form.getlist('modificar'),request.form.getlist('eliminar')))
        Rol.nuevo(db, rol, det_raw)
        return redirect(url_for('tipo_user'))
    else: 
        data, data_det, permisos = Rol.ver(db,0)
        return render_template('/Tablas/roles.html', title="Historial de Ingresos", data="", permisos="", data_det=data_det)

#------------------AUDITORÍA---------------------#

@app.route('/auditoria', methods=['GET', 'POST'])
@login_required
@role_required(['admin'])
def auditoria():
    response = Auditoria.get_tabla(db)
    response["permisos"] = "0,0,0,0"
    return render_template('table.html', title="Auditoria", data=response)

@app.route('/auditoria/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin'])
def ver_auditoria(id):
    data, data_det, permisos = Auditoria.ver(db,id)
    return render_template('/Tablas/auditoria.html', title="Auditoria", data=data, data_det=data_det, permisos=permisos)

#------------------ASISTENCIA---------------------#

@app.route('/asistencias', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def asistencia():
    response = Asistencia.get_tabla(db)
    return render_template('table.html', title="Asistencia", data=response)

@app.route('/asistencias/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def ver_asistencia(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_delete":
            Asistencia.delete(db, id)
        return redirect(url_for('asistencia'))
    else:
        data, data_det, permisos = Asistencia.ver(db,id)
        data_sec = Grados.get_tabla_raw(db)
        data_sec_2, data_sec_3 = Prof_materias.ver_raw(db)
        data_sec_4 = Horario.get_tabla_raw(db)
        permisos = (0,1)
        return render_template('/Tablas/asistencias.html', title="Asistencia", data=data, 
                               data_det=data_det, data_sec=data_sec, data_sec_2=data_sec_2, 
                               data_sec_3=data_sec_3, data_sec_4 = data_sec_4, permisos=permisos)

@app.route('/new_asistencias', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def add_asistencia():
    if request.method == "POST":
        asistencia = Asistencia(0, request.form["fecha"], request.form["horario"])
        presencia = set(zip(request.form.getlist('id_det'),request.form.getlist('asistencia')))

        Asistencia.nuevo(db, asistencia, presencia)
        return redirect(url_for('asistencia'))
    else: 
        data_sec = Grados.get_tabla_raw(db)
        data_sec_2, data_sec_3 = Prof_materias.ver_raw(db)
        data_sec_4 = Horario.get_tabla_raw(db)
        data_det = Alumnos.get_tabla_raw(db)
        return render_template('/Tablas/asistencias.html', title="Asistencia", data="", 
                               data_det=data_det, data_sec=data_sec, data_sec_2=data_sec_2, 
                               data_sec_3=data_sec_3, data_sec_4 = data_sec_4, permisos="")

#------------------PLAN DIARIO---------------------#

@app.route('/plan_diario', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def plan_diario():
    response = Plan_diario.get_tabla(db)
    return render_template('table.html', title="Plan Diario", data=response)

@app.route('/plan_diario/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def ver_plan_diario(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            estado = 0
            if session["rol"] in ['admin','directivo']:
                estado = request.form["aprob"]
            plan = Plan_diario(id, request.form["grado"], request.form["profesor"],request.form["materias"],request.form["titulo"],request.form["fecha"],request.form["descripcion"], estado)
            print(estado)
            anexo = request.files['anexo']
            anexo = limpia_arch(anexo)
            anexo = convierte_img_a_64_uniq(anexo)

            Plan_diario.update(db, plan, anexo)
            return redirect(url_for('plan_diario'))
        elif request.form["btn_submit"] == "btn_delete":
            Plan_diario.delete(db, id)
        return redirect(url_for('plan_diario'))
    else:
        data, permisos = Plan_diario.ver(db,id)
        data_sec = Grados.get_tabla_raw(db)
        data_sec_2, data_sec_3 = Prof_materias.ver_raw(db)
        return render_template('/Tablas/plan_diario.html', title="Plan diario", data=data, 
                               data_sec=data_sec, data_sec_2=data_sec_2, data_sec_3=data_sec_3,
                               permisos=permisos)

@app.route('/new_plan_diario', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def add_plan_diario():
    if request.method == "POST":
        plan = Plan_diario(0, request.form["grado"], request.form["profesor"],request.form["materias"],request.form["titulo"],request.form["fecha"],request.form["descrip"])
        anexo = request.files['anexo']
        anexo = limpia_arch(anexo)
        anexo = convierte_img_a_64_uniq(anexo)
        Plan_diario.nuevo(db, plan, anexo)
        return redirect(url_for('plan_diario'))
    else: 
        data_sec = Grados.get_tabla_raw(db)
        data_sec_2, data_sec_3 = Prof_materias.ver_raw(db)
        return render_template('/Tablas/plan_diario.html', title="Plan diario", data="", 
                               data_sec=data_sec, data_sec_2=data_sec_2, data_sec_3=data_sec_3,
                               permisos="")

#------------------PROCESOS(TAREAS)---------------------#

@app.route('/procesos', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def procesos():
    response = Procesos.get_tabla(db)
    return render_template('table.html', title="Procesos", data=response)

@app.route('/procesos/<id>', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def ver_procesos(id):
    if request.method == "POST":
        if request.form["btn_submit"] == "btn_editar":
            proceso = Procesos(id, request.form["grado"], request.form["materias"],request.form["profesor"],request.form["titulo"],
                           request.form["tot_punt"],request.form["fecha"],request.form["fecha_ent"],
                           request.form["tipo_proc"], request.form["etapa"], request.form["capacidad"])
            data_sec_7 = Indicadores.get_tabla_raw_x_proc(db, id)
            
            alums = request.form.getlist("id_alum")

            indic_grados = NULL

            for index, ind in enumerate(data_sec_7):
                aux = request.form.getlist(f"ind_{ind[0]}")
                if index==0:
                    indic_grados = indic_grados, aux
                    indic_grados = indic_grados[1:len(indic_grados)][0]
                else:
                    indic_grados = zip(*zip(*indic_grados), aux)
                    if index == len(data_sec_7)-1:
                        indic_grados = list(zip(alums,*zip(*indic_grados)))
            
            Procesos.update(db, proceso, indic_grados)
            return redirect(url_for('procesos'))
        elif request.form["btn_submit"] == "btn_delete":
            Procesos.delete(db, id)
        return redirect(url_for('procesos'))
    else:
        data, data_det, permisos = Procesos.ver(db,id)
        data_sec = Grados.get_tabla_raw(db)
        data_sec_2, data_sec_3 = Prof_materias.ver_raw(db)
        data_sec_4 = Tipo_procesos.get_tabla_raw(db)
        data_sec_6 = Alumnos.get_tabla_raw_x_grado(db, data[1])
        data_sec_7 = Indicadores.get_tabla_raw_x_proc(db, id)
        print(data_det)
        return render_template('/Tablas/procesos.html', title="Procesos", data=data, data_det=data_det,
                               data_sec=data_sec, data_sec_2=data_sec_2, data_sec_3=data_sec_3,
                               data_sec_4=data_sec_4, data_sec_5="", data_sec_6=data_sec_6, data_sec_7=data_sec_7,
                               permisos=permisos)

@app.route('/new_procesos', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def add_procesos():
    if request.method == "POST":
        proceso = Procesos(0, request.form["grado"], request.form["materias"],request.form["profesor"],request.form["titulo"],
                           request.form["tot_punt"],request.form["fecha"],request.form["fecha_ent"],
                           request.form["tipo_proc"], request.form["etapa"], request.form["capacidad"])
        indic_grados = request.form.getlist("id_det_ind")
        Procesos.nuevo(db, proceso, indic_grados)
        return redirect(url_for('procesos'))
    else: 
        data_sec = Grados.get_tabla_raw(db)
        data_sec_2, data_sec_3 = Prof_materias.ver_raw(db)
        data_sec_4 = Tipo_procesos.get_tabla_raw(db)
        data_sec_5 = Indicadores.get_tabla(db)
        return render_template('/Tablas/procesos.html', title="Procesos", data="", 
                               data_sec=data_sec, data_sec_2=data_sec_2, data_sec_3=data_sec_3,
                               data_sec_4=data_sec_4, data_sec_5=data_sec_5, data_sec_6="", data_sec_7="",
                               permisos="")


#------------------PLANILLAS---------------------#
@app.route('/planillas', methods=['GET', 'POST'])
@login_required
@role_required(['admin','directivo', 'profesor'])
def planillas():
    if request.method == "POST":
        grado = request.form["grado"]
        materia = request.form["materias"]
        profesor = request.form["profesor"]
        etapa = request.form["etapa"]
        anho = request.form["anho"]
        tipo_plan = request.form["tipo_plani"]

        if int(tipo_plan) == 1: 
            cabecera, data, data_det, colums = Procesos.ver_para_planilla_materia(db,grado, profesor, materia, etapa, anho)
            if not cabecera is None:
                planilla_proc_detallado(cabecera, data, data_det, colums)
                return redirect(url_for('descarga_planilla',filename=f"Planilla_{cabecera[2]}.xlsx"))
            else:
                err = {"title": "Error!",
                    "detalle":  str("No hay procesos!")}
                flash(err)
        elif int(tipo_plan) == 2: 
            cabecera, data_det, colums = Procesos.ver_para_planilla_grado(db,grado, profesor, materia, etapa, anho)
            if not cabecera is None:
                planilla_proc_grado(cabecera, data_det, colums)
                return redirect(url_for('descarga_planilla',filename=f"Planilla_{cabecera[0]}.xlsx"))
            else:
                err = {"title": "Error!",
                    "detalle":  str("No hay procesos!")}
                flash(err)
    data_sec = Grados.get_tabla_raw(db)
    data_sec_2, data_sec_3 = Prof_materias.ver_raw(db)
    return render_template('Tablas/planillas.html', title="Planillas", data_sec=data_sec, data_sec_2=data_sec_2, data_sec_3=data_sec_3)

#------------------MISC.---------------------#

@app.route('/profesores/legajo/dowload/<id>', methods=['GET', 'POST'])
@login_required
def descarga_legajo(id):
    data = Legajo.get_to_descargar(db, id)
    return convierte_64_a_img(data)

@app.route('/plan_diario/anexo/dowload/<id>', methods=['GET', 'POST'])
@login_required
def descarga_anexo(id):
    data = Plan_diario.get_to_descargar(db, id)
    return convierte_64_a_img(data)

@app.route('/<path:filename>', methods=['GET', 'POST'])
@login_required
def descarga_planilla(filename):
    print(app.root_path)
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(full_path,filename, as_attachment=True)

#------------------ERRORES---------------------#

def status_401(error):
    return redirect(url_for('login'))

def status_403(error):
    print("ERRORRR")
    return render_template('404.html'), 403

def status_404(error):
    #flash("Parece que no iniciaste sesión...")
    return render_template('404.html'), 404

#------------------INICIAR---------------------#

if __name__ == '__main__':
    app.register_error_handler(401, status_401)
    app.register_error_handler(403, status_403)
    app.register_error_handler(404, status_404)
    app.run(host="0.0.0.0")
