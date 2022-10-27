import json
from flask import flash

class Materia():
    tablename = 'materias'

    def __init__(self, idmateria, nombre, descripcion=""):
        self.id = idmateria
        self.nombre = nombre
        self.descripcion = descripcion
    
    def nuevo(db, materia):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO %s (nombre, descripcion) 
                        VALUES (%s,%s)"""
            val = Materia.tablename, materia.nombre, materia.descripcion
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
            sql = f"SELECT * from {Materia.tablename} WHERE idmateria = {id} and estado = 1"
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
            sql = """UPDATE %s
                    SET nombre = %s, descripcion = %s
                    WHERE idmateria = %s;"""
            val = Materia.tablename, materia.nombre, materia.descripcion, materia.id
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
            sql = f"UPDATE {Materia.tablename} SET estado = 0 WHERE idmateria = {id};"
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
    tablename = 'nivel_escolar'

    def __init__(self, idnivel_escolar, nombre, exigencia):
        self.id  = idnivel_escolar 
        self.nombre = nombre
        self.exigencia  = exigencia 
    
    def nuevo(db, nivel_escolar):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO %s (nombre, exigencia) 
                        VALUES (%s,%s)"""
            val = Nivel_escolar.tablename, nivel_escolar.nombre, nivel_escolar.exigencia
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
            sql = f"SELECT * from {Nivel_escolar.tablename} WHERE idnivel_escolar = {id}"
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
            sql = """UPDATE %s
                    SET nombre = %s, exigencia = %s
                    WHERE idnivel_escolar = %s;"""
            val = Nivel_escolar.tablename, nivel_escolar.nombre, nivel_escolar.exigencia, nivel_escolar.id
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
    tablename = 'secciones'

    def __init__(self, idseccion, nombre):
        self.id = idseccion
        self.nombre = nombre
    
    def nuevo(db, seccion):
        cursor = db.connection.cursor()
        try:
            sql = f"""INSERT INTO %s (nombre,) 
                        VALUES (%s)"""
            val = Secciones.tablename, seccion.nombre, seccion.descripcion
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
            sql = f"SELECT * from {Secciones.tablename} WHERE idseccion = {id}"
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
            sql = """UPDATE %s
                    SET nombre = %s
                    WHERE idseccion = %s;"""
            val = Secciones.tablename, seccion.nombre, seccion.id
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
    tablename = 'tutores'

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
            sql = f"""INSERT INTO %s (nombres, apellidos, documento, celular, email, domicilio) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            val = Tutor.tablename, tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio
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
            sql = f"SELECT * from {Tutor.tablename} WHERE idtutor = {id} and estado = 1"
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
            sql = """UPDATE %s
                    SET idtutor = %s, nombre = %s, apellido = %s, documento = %s, celular = %s, email = %s, domicilio = %s
                    WHERE idtutor = %s;"""
            val = Tutor.tablename, tutor.nombre, tutor.apellido, tutor.documento, tutor.celular, tutor.email, tutor.domicilio, tutor.id
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
            sql = f"UPDATE {Tutor.tablename} SET estado = 0 WHERE idtutor = {id};"
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