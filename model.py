import json
from flask import flash

class Materia():
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
            return results
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
            return results
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
            return results
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
                        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
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
            return results
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