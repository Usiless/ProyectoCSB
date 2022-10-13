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
        try:
            sql = f"SELECT * from materias WHERE idmateria = {id}"
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
                        'tabla': f"{tabla}",}
            return response
        except db.connection.Error as error :
            err = {"title": "Cambio en la base fallido!",
                   "detalle":  str(error)}
            flash(err)
            db.connection.rollback()
            return None


