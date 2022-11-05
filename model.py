import json
from flask import flash, session

def get_tabla(db, columnas, col, tabla, orden, estado):
    permisos = obtener_permisos(db, tabla)
    try:
        sql = f"SELECT {columnas} FROM {tabla} {'WHERE estado = 1 ' * estado}ORDER BY {orden} asc;"
        cursor = db.connection.cursor()
        cursor.execute(sql)
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
                    'tabla': f"{tabla}",
                    'orden': col,
                    'permisos': permisos}
        return response
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def nuevo(db,val, nombre_tabla, cols):
    cursor = db.connection.cursor()
    cantidad_col = cols.count(", ")
    try:
        if cantidad_col == 0:
            sql = f"INSERT INTO {nombre_tabla} ({cols}) VALUES ('{val}')"
            cursor.execute(sql)
        else:
            sql = f"INSERT INTO {nombre_tabla} ({cols}) VALUES ({cantidad_col * '%s, '}%s)"
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
            sql = f"SELECT * from {nombre_tabla} WHERE {col_id} = {id} {'AND estado = 1' * estado}"
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
    cols_act = cols_act.replace(", ", " = %s, " )

    try:
        sql = f"UPDATE {nombre_tabla} SET {cols_act} = %s WHERE {col_id} = %s;"
        print(sql)
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
    orden = "idmateria"
    col_id = "idmateria"
    cols = "nombre, descripcion"
    elim_log = 1

    cols_def = col_id + ", nombre"
    tabla_col_def = ["ID", "Nombre"]

    def __init__(self, idmateria, nombre, descripcion=""):
        self.id = idmateria
        self.nombre = nombre
        self.descripcion = descripcion

    def get_tabla(db):
        response = get_tabla(db, Materia.cols_def, Materia.tabla_col_def, Materia.nombre_tabla, Materia.orden, Materia.elim_log)
        return response
    
    def nuevo(db, materia):
        val = materia.nombre, materia.descripcion
        nuevo(db, val, Materia.nombre_tabla, Materia.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Materia.nombre_tabla)
        datos = ver(db, id, Materia.nombre_tabla, Materia.col_id, Materia.elim_log)
        return datos, permisos

    def update(db, materia):
        val = materia.nombre, materia.descripcion, materia.id
        update(db, val, Materia.nombre_tabla, Materia.cols, Materia.col_id)

    def delete(db, id):
        delete_logic(db, Materia.nombre_tabla, Materia.col_id, id)

class Nivel_escolar():
    nombre_tabla = "nivel_escolar"
    orden = "idnivel_escolar"
    col_id = "idnivel_escolar"
    cols = "nombre, exigencia"
    elim_log = 0
    
    cols_def = col_id + ", nombre, exigencia"
    tabla_col_def = ["ID", "Nombre", "Exigencia"]

    def __init__(self, idnivel_escolar, nombre, exigencia):
        self.id  = idnivel_escolar 
        self.nombre = nombre
        self.exigencia  = exigencia

    def get_tabla(db):
        response = get_tabla(db, Nivel_escolar.cols_def, Nivel_escolar.tabla_col_def, Nivel_escolar.nombre_tabla, Nivel_escolar.orden, Nivel_escolar.elim_log)
        return response
    
    def nuevo(db, nivel_escolar):
        val = nivel_escolar.nombre, nivel_escolar.exigencia
        nuevo(db, val, Nivel_escolar.nombre_tabla, Nivel_escolar.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Nivel_escolar.nombre_tabla)
        datos = ver(db, id, Nivel_escolar.nombre_tabla, Nivel_escolar.col_id, Nivel_escolar.elim_log)
        return datos, permisos

    def update(db, nivel_escolar):
        val = nivel_escolar.nombre, nivel_escolar.exigencia
        update(db, val, Nivel_escolar.nombre_tabla, Nivel_escolar.cols, Nivel_escolar.col_id)

class Secciones():
    nombre_tabla = "secciones"
    orden = "idseccion"
    col_id = "idseccion"
    cols = "nombre"
    elim_log = 0

    cols_def = col_id + ", nombre"
    tabla_col_def = ["ID", "Nombre"]

    def __init__(self, idseccion, nombre):
        self.id = idseccion
        self.nombre = str(nombre)

    def get_tabla(db):
        response = get_tabla(db, Secciones.cols_def, Secciones.tabla_col_def, Secciones.nombre_tabla, Secciones.orden, Secciones.elim_log)
        return response
    
    def nuevo(db, seccion):
        val = seccion.nombre
        nuevo(db, val, Secciones.nombre_tabla, Secciones.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Secciones.nombre_tabla)
        datos = ver(db, id, Secciones.nombre_tabla, Secciones.col_id, Secciones.elim_log)
        return datos, permisos

    def update(db, seccion):
        val = seccion.nombre, seccion.id
        update(db, val, Secciones.nombre_tabla, Secciones.cols, Secciones.col_id)

class Tutor():
    nombre_tabla = "tutores"
    orden = "idtutor"
    col_id = "idtutor"
    cols = "nombres, apellidos, documento, celular, email, domicilio"
    elim_log = 1

    cols_def = col_id + ", nombres, apellidos"
    tabla_col_def = ["ID", "Nombre", "Apellido"]

    def __init__(self, idtutor, nombre, apellido, documento, celular, email, domicilio):
        self.id = idtutor
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.celular = celular
        self.email = email
        self.domicilio = domicilio

    def get_tabla(db):
        response = get_tabla(db, Tutor.cols_def, Tutor.tabla_col_def, Tutor.nombre_tabla, Tutor.orden, Tutor.elim_log)
        return response
    
    def nuevo(db, tutor):
        val = tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio
        nuevo(db, val, Tutor.nombre_tabla, Tutor.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Tutor.nombre_tabla)
        datos = ver(db, id, Tutor.nombre_tabla, Tutor.col_id, Tutor.elim_log)
        return datos, permisos

    def update(db, tutor):
        val = tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio, tutor.id
        update(db, val, Tutor.nombre_tabla, Tutor.cols, Tutor.col_id)

    def delete(db, id):
        delete_logic(db, Tutor.nombre_tabla, Tutor.col_id, id)

class Gravedad():
    nombre_tabla = "gravedad"
    orden = "idgravedad"
    col_id = "idgravedad"
    cols = "nombre, descripcion"
    elim_log = 0

    cols_def = col_id + ", nombre"
    tabla_col_def = ["ID", "Nombre"]

    def __init__(self, idgravedad, nombre, descripcion=""):
        self.id = idgravedad
        self.nombre = nombre
        self.descripcion = descripcion

    def get_tabla(db):
        response = get_tabla(db, Gravedad.cols_def, Gravedad.tabla_col_def, Gravedad.nombre_tabla, Gravedad.orden, Gravedad.elim_log)
        return response
    
    def nuevo(db, gravedad):
        val = gravedad.nombre, gravedad.descripcion
        nuevo(db, val, Gravedad.nombre_tabla, Gravedad.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Gravedad.nombre_tabla)
        datos = ver(db, id, Gravedad.nombre_tabla, Gravedad.col_id, Gravedad.elim_log)
        return datos, permisos

    def update(db, gravedad):
        val = gravedad.nombre, gravedad.descripcion, gravedad.id   
        update(db, val, Gravedad.nombre_tabla, Gravedad.cols, Gravedad.col_id)

class Tipo_procesos():
    nombre_tabla = "tipo_procesos"
    orden = "idtipo_proceso"
    col_id = "idtipo_proceso"
    cols = "descripcion"
    elim_log = 0

    cols_def = col_id + ", descripcion"
    tabla_col_def = ["ID", "Descripcion"]

    def __init__(self, idtipo_procesos, descripcion):
        self.id = idtipo_procesos
        self.descripcion = descripcion

    def get_tabla(db):
        response = get_tabla(db, Tipo_procesos.cols_def, Tipo_procesos.tabla_col_def, Tipo_procesos.nombre_tabla, Tipo_procesos.orden, Tipo_procesos.elim_log)
        return response
    
    def nuevo(db, tipo_proceso):
        val = tipo_proceso.descripcion
        nuevo(db, val, Tipo_procesos.nombre_tabla, Tipo_procesos.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Tipo_procesos.nombre_tabla)
        datos = ver(db, id, Tipo_procesos.nombre_tabla, Tipo_procesos.col_id, Tipo_procesos.elim_log)
        return datos, permisos

    def update(db, tipo_proceso):
        val = tipo_proceso.descripcion  
        update(db, val, Tipo_procesos.nombre_tabla, Tipo_procesos.cols, Tipo_procesos.col_id)

class Visitante():
    nombre_tabla = "visitantes"
    col_id = "idvisitante"
    cols = "nombres, apellidos, telefono, estado"
    elim_log = 1    
    
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
        datos = ver(db, id, Visitante.nombre_tabla, Visitante.col_id, Visitante.elim_log)
        return datos, permisos

    def update(db, visitante):
        val = visitante.nombres, visitante.apellidos, visitante.telefono
        update(db, val, Visitante.nombre_tabla, Visitante.cols, Visitante.col_id)

    def delete(db, id):
        delete_logic(db, Visitante.nombre_tabla, Visitante.col_id, id)

class Historial_ingreso():
    nombre_tabla = "historial_de_ingresos"
    col_id = "idhistorial_de_ingreso"
    cols = "fecha, descripcion"
    elim_log = 0

    def __init__(self, idhistorial_ingreso, fecha, descripcion=""):
        self.id = idhistorial_ingreso
        self.fecha = fecha
        self.descripcion = descripcion

    def nuevo(db, historial_ingreso):
        val = historial_ingreso.fecha, historial_ingreso.descripcion
        nuevo(db, val, Historial_ingreso.nombre_tabla, Historial_ingreso.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Historial_ingreso.nombre_tabla)
        datos = ver(db, id, Historial_ingreso.nombre_tabla, Historial_ingreso.col_id, Historial_ingreso.elim_log)
        return datos, permisos

    def update(db, historial_ingreso):
        val = historial_ingreso.fecha, historial_ingreso.descripcion
        update(db, val, Historial_ingreso.nombre_tabla, Historial_ingreso.cols, Historial_ingreso.col_id)

class Indicadores():
    nombre_tabla = "idindicadores"
    col_id = "idindicadores"
    cols = "descripción"
    elim_log = 0

    def __init__(self, idmateria, descripcion):
        self.id = idmateria
        self.descripcion = descripcion
    
    def nuevo(db, indicadores):
        val = indicadores.descripcion
        nuevo(db, val, Indicadores.nombre_tabla, Indicadores.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Indicadores.nombre_tabla)
        datos = ver(db, id, Indicadores.nombre_tabla, Indicadores.col_id, Indicadores.elim_log)
        return datos, permisos

    def update(db, indicadores):
        val = indicadores.descripcion
        update(db, val, Indicadores.nombre_tabla, Indicadores.cols, Indicadores.col_id)