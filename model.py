from asyncio.windows_events import NULL
from http.client import responses
import json
from flask import flash, session

def get_tabla(db, columnas, col, tabla, orden, estado):
    try:
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT {columnas} FROM {tabla} {estado} ORDER BY {orden} asc;")
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
            print(a)
            a = str(str(a).replace("'", f"{chr (34)}"))
            print(a)
            data = a
        response = {'data': json.loads(data),
                    'tabla': f"{tabla}",
                    'orden': col,}
        print(data)
        print(response)
        return response
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def nuevo(db,val, nombre_tabla, cols):
    cursor = db.connection.cursor()
    try:
        sql = f"INSERT INTO {nombre_tabla} ({cols}) VALUES (%s,%s)"
        cursor.execute(sql, val)
        db.connection.commit()
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None

def ver(db, id, nombre_tabla, col_id, estado):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from {nombre_tabla} WHERE {col_id} = {id} {estado}"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None

def obtener_permisos(db, nombre_tabla):
    cursor = db.connection.cursor()
    try:
        user_id = session["_user_id"]
        sql = f"""SELECT actualizar, borrar, crear, leer
                FROM csb_prov.permisos, csb_prov.tipo_user, csb_prov.users, csb_prov.tablas 
                where csb_prov.users.idtipo_user = csb_prov.tipo_user.idtipo_user 
                and csb_prov.permisos.idtabla = csb_prov.tablas.idtabla 
                and csb_prov.users.id_user = {user_id}
                and csb_prov.tablas.nombre = "{nombre_tabla}";"""
        cursor.execute(sql)
        permisos = cursor.fetchone()
        return permisos
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def update(db, val, nombre_tabla, cols_act, col_id):
        cursor = db.connection.cursor()
        try:
            sql = f"UPDATE {nombre_tabla} SET {cols_act} WHERE {col_id} = %s;"
            cursor.execute(sql, val)
            db.connection.commit()
            err = {"title": "Guardado!",}
            flash(err)
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

def delete_logic(db, nombre_tabla, col_id, id):
    cursor = db.connection.cursor()
    try:
        sql = f"UPDATE {nombre_tabla} SET estado = 0 WHERE {col_id} = {id};"
        cursor.execute(sql)
        db.connection.commit()
        err = {"title": "Eliminado!",}
        flash(err)
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None

def delete_fis(db, nombre_tabla, col_id, id):
    cursor = db.connection.cursor()
    try:
        sql = f"DELETE FROM {nombre_tabla} WHERE {col_id} = {id};"
        cursor.execute(sql)
        db.connection.commit()
        err = {"title": "Eliminado!",}
        flash(err)
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None


class Materia():
    nombre_tabla = "materias"
    col_id = "idmateria"
    cols = "nombre, descripcion"
    cols_act = "nombre = %s, descripcion = %s"
    estado = " and estado = 1"

    def __init__(self, idmateria, nombre, descripcion=""):
        self.id = idmateria
        self.nombre = nombre
        self.descripcion = descripcion
    
    def nuevo(db, materia):
        val = materia.nombre, materia.descripcion
        nuevo(db, val, Materia.nombre_tabla, Materia.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Materia.nombre_tabla)
        datos = ver(db, id, Materia.nombre_tabla, Materia.col_id, Materia.estado)
        return datos, permisos

    def update(db, materia):
        val = materia.nombre, materia.descripcion, materia.id
        update(db, val, Materia.nombre_tabla, Materia.cols_act, Materia.col_id)

    def delete(db, id):
        delete_logic(db, Materia.nombre_tabla, Materia.col_id, id)

class Nivel_escolar():
    nombre_tabla = "nivel_escolar"
    col_id = "idnivel_escolar"
    cols = "nombre, exigencia"
    cols_act = "nombre = %s, exigencia = %s"
    estado = ""

    def __init__(self, idnivel_escolar, nombre, exigencia):
        self.id  = idnivel_escolar 
        self.nombre = nombre
        self.exigencia  = exigencia 
    
    def nuevo(db, nivel_escolar):
        val = nivel_escolar.nombre, nivel_escolar.exigencia
        nuevo(db, val, Nivel_escolar.nombre_tabla, Nivel_escolar.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Nivel_escolar.nombre_tabla)
        datos = ver(db, id, Nivel_escolar.nombre_tabla, Nivel_escolar.col_id, Nivel_escolar.estado)
        return datos, permisos

    def update(db, nivel_escolar):
        val = nivel_escolar.nombre, nivel_escolar.exigencia
        update(db, val, Nivel_escolar.nombre_tabla, Nivel_escolar.cols_act, Nivel_escolar.col_id)

class Secciones():
    nombre_tabla = "secciones"
    col_id = "idseccion"
    cols = "nombre"
    cols_act = "nombre = %s"
    estado = ""

    def __init__(self, idseccion, nombre):
        self.id = idseccion
        self.nombre = nombre
    
    def nuevo(db, seccion):
        val = seccion.nombre, seccion.descripcion
        nuevo(db, val, Secciones.nombre_tabla, Secciones.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Secciones.nombre_tabla)
        datos = ver(db, id, Secciones.nombre_tabla, Secciones.col_id, Secciones.estado)
        return datos, permisos

    def update(db, seccion):
        val = seccion.nombre, seccion.descripcion, seccion.id
        update(db, val, Secciones.nombre_tabla, Secciones.cols_act, Secciones.col_id)

class Tutor():
    nombre_tabla = "tutores"
    col_id = "idtutor"
    cols = "nombres, apellidos, documento, celular, email, domicilio"
    cols_act = "nombre = %s, apellido = %s, documento = %s, celular = %s, email = %s, domicilio = %s"
    estado = " and estado = 1"

    def __init__(self, idtutor, nombre, apellido, documento, celular, email, domicilio):
        self.id = idtutor
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.celular = celular
        self.email = email
        self.domicilio = domicilio
    
    def nuevo(db, tutor):
        val = tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio, tutor.id
        nuevo(db, val, Tutor.nombre_tabla, Tutor.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Tutor.nombre_tabla)
        datos = ver(db, id, Tutor.nombre_tabla, Tutor.col_id, Tutor.estado)
        return datos, permisos

    def update(db, tutor):
        val = tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio, tutor.id
        update(db, val, Tutor.nombre_tabla, Tutor.cols_act, Tutor.col_id)

    def delete(db, id):
        delete_logic(db, Tutor.nombre_tabla, Tutor.col_id, id)

class Gravedad():
    nombre_tabla = "gravedad"
    col_id = "idgravedad"
    cols = "nombre, descripcion"
    cols_act = "nombre = %s, descripcion = %s"
    estado = ""

    def __init__(self, idgravedad, nombre, descripcion=""):
        self.id = idgravedad
        self.nombre = nombre
        self.descripcion = descripcion
    
    def nuevo(db, gravedad):
        val = gravedad.nombre, gravedad.descripcion, gravedad.id
        nuevo(db, val, Gravedad.nombre_tabla, Gravedad.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Gravedad.nombre_tabla)
        datos = ver(db, id, Gravedad.nombre_tabla, Gravedad.col_id, Gravedad.estado)
        return datos, permisos

    def update(db, gravedad):
        val = gravedad.nombre, gravedad.descripcion, gravedad.id   
        update(db, val, Gravedad.nombre_tabla, Gravedad.cols_act, Gravedad.col_id)

class Tipo_procesos():
    nombre_tabla = "tipo_procesos"
    col_id = "idtipo_procesos"
    cols = "descripcion"
    cols_act = "descripcion = %s"
    estado = ""

    def __init__(self, idtipo_procesos, descripcion):
        self.id = idtipo_procesos
        self.descripcion = descripcion
    
    def nuevo(db, tipo_proceso):
        val = tipo_proceso.descripcion
        nuevo(db, val, Tipo_procesos.nombre_tabla, Tipo_procesos.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Tipo_procesos.nombre_tabla)
        datos = ver(db, id, Tipo_procesos.nombre_tabla, Tipo_procesos.col_id, Tipo_procesos.estado)
        return datos, permisos

    def update(db, tipo_proceso):
        val = tipo_proceso.descripcion  
        update(db, val, Tipo_procesos.nombre_tabla, Tipo_procesos.cols_act, Tipo_procesos.col_id)

class Visitante():
    nombre_tabla = "visitantes"
    col_id = "idvisitante"
    cols = "nombres, apellidos, telefono, estado"
    cols_act = "nombres = %s, apellidos = %s, telefono = %s, estado = %s"
    estado = " and estado = 1"    
    
    def __init__(self, idvisitante, nombres, apellidos, telefono):
        self.id = idvisitante
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono

    def nuevo(db, visitante):
        val = visitante.nombres, visitante.apellidos, visitante.telefono
        nuevo(db, val, Visitante.nombre_tabla, Visitante.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Visitante.nombre_tabla)
        datos = ver(db, id, Visitante.nombre_tabla, Visitante.col_id, Visitante.estado)
        return datos, permisos

    def update(db, visitante):
        val = visitante.nombres, visitante.apellidos, visitante.telefono
        update(db, val, Visitante.nombre_tabla, Visitante.cols_act, Visitante.col_id)

    def delete(db, id):
        delete_logic(db, Visitante.nombre_tabla, Visitante.col_id, id)

class Historial_ingreso():
    nombre_tabla = "historial_de_ingresos"
    col_id = "idhistorial_de_ingreso"
    cols = "fecha, descripcion"
    cols_act = "fecha = %s, descripcion = %s"
    estado = ""

    def __init__(self, idhistorial_ingreso, fecha, descripcion=""):
        self.id = idhistorial_ingreso
        self.fecha = fecha
        self.descripcion = descripcion

    def nuevo(db, historial_ingreso):
        val = historial_ingreso.fecha, historial_ingreso.descripcion
        nuevo(db, val, Historial_ingreso.nombre_tabla, Historial_ingreso.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Historial_ingreso.nombre_tabla)
        datos = ver(db, id, Historial_ingreso.nombre_tabla, Historial_ingreso.col_id, Historial_ingreso.estado)
        return datos, permisos

    def update(db, historial_ingreso):
        val = historial_ingreso.fecha, historial_ingreso.descripcion
        update(db, val, Historial_ingreso.nombre_tabla, Historial_ingreso.cols_act, Historial_ingreso.col_id)

class Indicadores():
    nombre_tabla = "idindicadores"
    col_id = "idindicadores"
    cols = "descripción"
    cols_act = "descripción = %s"
    estado = ""

    def __init__(self, idmateria, descripcion):
        self.id = idmateria
        self.descripcion = descripcion
    
    def nuevo(db, indicadores):
        val = indicadores.descripcion
        nuevo(db, val, Indicadores.nombre_tabla, Indicadores.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Indicadores.nombre_tabla)
        datos = ver(db, id, Indicadores.nombre_tabla, Indicadores.col_id, Indicadores.estado)
        return datos, permisos

    def update(db, indicadores):
        val = indicadores.descripcion
        update(db, val, Indicadores.nombre_tabla, Indicadores.cols_act, Indicadores.col_id)