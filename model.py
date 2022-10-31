from asyncio.windows_events import NULL
from http.client import responses
import json
from flask import flash

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

class Materia():
    permisos = {"eliminar": 1,}
    def __init__(self, idmateria, nombre, descripcion=""):
        self.id = idmateria
        self.nombre = nombre
        self.descripcion = descripcion
    
    def nuevo(db, materia):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO materias (nombre, descripcion) 
                        VALUES (%s,%s)"""
            val = materia.nombre, materia.descripcion
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from materias WHERE idmateria = {id} and estado = 1"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Materia.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, materia):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE materias
                    SET nombre = %s, descripcion = %s
                    WHERE idmateria = %s;"""
            val = materia.nombre, materia.descripcion, materia.id
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

    def delete(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"UPDATE materias SET estado = 0 WHERE idmateria = {id};"
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

class Nivel_escolar():
    permisos = {"eliminar": "",}
    def __init__(self, idnivel_escolar, nombre, exigencia):
        self.id  = idnivel_escolar 
        self.nombre = nombre
        self.exigencia  = exigencia 
    
    def nuevo(db, nivel_escolar):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO nivel_escolar (nombre, exigencia) 
                        VALUES (%s,%s)"""
            val = nivel_escolar.nombre, nivel_escolar.exigencia
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from nivel_escolar WHERE idnivel_escolar = {id}"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Nivel_escolar.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, nivel_escolar):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE nivel_escolar
                    SET nombre = %s, exigencia = %s
                    WHERE idnivel_escolar = %s;"""
            val = nivel_escolar.nombre, nivel_escolar.exigencia, nivel_escolar.id
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

class Secciones():
    permisos = {"eliminar": "",}
    def __init__(self, idseccion, nombre):
        self.id = idseccion
        self.nombre = nombre
    
    def nuevo(db, seccion):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO secciones (nombre,) 
                        VALUES (%s)"""
            val = seccion.nombre, seccion.descripcion
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from secciones WHERE idseccion = {id}"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Secciones.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, seccion):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE secciones
                    SET nombre = %s
                    WHERE idseccion = %s;"""
            val = seccion.nombre, seccion.id
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

class Tutor():
    permisos = {"eliminar": 1,}
    def __init__(self, idtutor, nombre, apellido, documento, celular, email, domicilio):
        self.id = idtutor
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.celular = celular
        self.email = email
        self.domicilio = domicilio
    
    def nuevo(db, tutor):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO tutores (nombres, apellidos, documento, celular, email, domicilio) 
                        VALUES (%s,%s,%s,%s,%s,%s)"""
            val = tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from tutores WHERE idtutor = {id} and estado = 1"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Tutor.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, tutor):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE tutores
                    SET idtutor = %s, nombre = %s, apellido = %s, documento = %s, celular = %s, email = %s, domicilio = %s
                    WHERE idtutor = %s;"""
            val = tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio, tutor.id
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

    def delete(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"UPDATE tutores SET estado = 0 WHERE idtutor = {id};"
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

class Gravedad():
    permisos = {"eliminar": "",}
    def __init__(self, idgravedad, nombre, descripcion=""):
        self.id = idgravedad
        self.nombre = nombre
        self.descripcion = descripcion
    
    def nuevo(db, gravedad):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO gravedad (nombre, descripcion) 
                        VALUES (%s,%s)"""
            val = gravedad.nombre, gravedad.descripcion
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from gravedad WHERE idgravedad = {id}"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Gravedad.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, gravedad):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE gravedad
                    SET nombre = %s, descripcion = %s
                    WHERE idgravedad = %s;"""
            val = gravedad.nombre, gravedad.descripcion, gravedad.id
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

class Tipo_procesos():
    permisos = {"eliminar": "",}
    def __init__(self, idtipo_procesos, nombre, descripcion=""):
        self.id = idtipo_procesos
        self.descripcion = descripcion
    
    def nuevo(db, tipo_procesos):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO tipo_procesos (descripcion) 
                        VALUES (%s,%s)"""
            val = tipo_procesos.descripcion
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from tipo_procesos WHERE idtipo_procesos = {id}"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Tipo_procesos.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, tipo_procesos):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE tipo_procesos
                    SET descripcion = %s
                    WHERE idtipo_procesos = %s;"""
            val = tipo_procesos.descripcion, tipo_procesos.id
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

class Visitante():
    permisos = {"eliminar": 1,}
    def __init__(self, idvisitante, nombres, apellidos, telefono):
        self.id = idvisitante
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
    
    def nuevo(db, visitante):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO visitantes (nombres, apellidos, telefono) 
                        VALUES (%s,%s)"""
            val = visitante.nombres, visitante.apellidos, visitante.telefono
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from visitantes WHERE idvisitante = {id} and estado = 1"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Visitante.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, visitante):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE visitantes
                    SET nombres = %s, apellidos = %s, telefono = %s
                    WHERE idvisitante = %s;"""
            val = visitante.nombres, visitante.apellidos, visitante.telefono, visitante.id
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

    def delete(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"UPDATE visitantes SET estado = 0 WHERE idvisitante = {id};"
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

class Historial_ingreso():
    permisos = {"eliminar": "",}
    def __init__(self, idhistorial_ingreso, fecha, descripcion=""):
        self.id = idhistorial_ingreso
        self.fecha = fecha
        self.descripcion = descripcion
    
    def nuevo(db, historial_ingreso):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO historial_ingresos (fecha, descripcion) 
                        VALUES (%s,%s)"""
            val = historial_ingreso.fecha, historial_ingreso.descripcion
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from historial_ingresos WHERE idhistorial_ingreso = {id}"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Historial_ingreso.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, historial_ingreso):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE historial_ingresos
                    SET fecha = %s, descripcion = %s
                    WHERE idhistorial_ingreso = %s;"""
            val = historial_ingreso.fecha, historial_ingreso.descripcion, historial_ingreso.id
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

class Indicadores():
    permisos = {"eliminar": "",}
    def __init__(self, idmateria, nombre, descripcion=""):
        self.id = idmateria
        self.nombre = nombre
    
    def nuevo(db, indicador):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO indicadores (descripcion) 
                        VALUES (%s,%s)"""
            val = indicador.descripcion
            cursor.execute(sql, val)
            db.connection.commit()
            return None
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None

    def ver(db, id):
        cursor = db.connection.cursor()
        try:
            sql = f"SELECT * from indicadores WHERE idmateria = {id}"
            cursor.execute(sql)
            results = cursor.fetchone()
            return results, Indicadores.permisos["eliminar"]
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None
    
    def update(db, indicador):
        cursor = db.connection.cursor()
        try:
            sql = """UPDATE indicadores
                    descripcion = %s
                    WHERE idmateria = %s;"""
            val = indicador.descripcion, indicador.id
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