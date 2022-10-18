import json
from flask import flash
class Materia():
    __tablename__ = 'materias'

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

    def ver(db, id):
        cursor = db.connection.cursor()
        sql = f"SELECT * from materias WHERE idmateria = {id}"
        cursor.execute(sql)
        results = cursor.fetchone()
        # sql = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='csb_prov' AND TABLE_NAME='materias'"
        # cursor.execute(sql)
        # columnas = cursor.fetchall()
        # cursor.close()
        # data = []
        # c=0
        # for row in columnas:
        #     data.append({f'{str(row[0])}': f"{results[c]}",})
        #     c+=1
        # data = str(data).replace('}, {', ', ')
        # data = json.dumps(data, separators=(',', ':'))
        # resultados = json.loads(data)
        # print(type(resultados))
        return results



