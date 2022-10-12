from flask import flash
class Materia():

    def __init__(self, idmateria, nombre, descripcion=""):
        self.id = idmateria
        self.nombre = nombre
        self.descripcion = descripcion
    
    def nuevo(db, materia):
        cursor = db.connection.cursor()
        try:
            sql = """INSERT INTO materias (nombre, descripcion) 
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


