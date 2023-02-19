import datetime
import json
from flask import flash, session
from flask_login import current_user

def get_tabla_custom_req(db, sql, tabla, col):
    permisos = obtener_permisos(db, tabla)
    try:
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

def get_tabla_custom_req_raw(db, sql, tabla):
    try:
        cursor = db.connection.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        cursor.close()
        return response
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None


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

def get_tabla_compleja(db, columnas, col, tabla, tabla_sec, orden, estado, filtro_val=""):
    permisos = obtener_permisos(db, tabla)
    nat_joins = ''
    for i in tabla_sec:
        nat_joins = nat_joins + f' NATURAL JOIN {i}'

    try:
        if filtro_val:
            sql = f"SELECT {columnas} FROM {tabla} {nat_joins} {'WHERE estado = 1 ' * estado} {'AND' * estado} {'WHERE' * (1 - estado)} {filtro_val} ORDER BY {orden} asc;"
        else:
            sql = f"SELECT {columnas} FROM {tabla} {nat_joins} {'WHERE estado = 1 ' * estado} ORDER BY {orden} asc;"
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

def get_tabla_compleja_raw(db, columnas, nombre_tabla, tabla_sec, estado, filtro_val=""):
        cursor = db.connection.cursor()
        try:
            if filtro_val:
                sql = f"SELECT {columnas} FROM {nombre_tabla} NATURAL JOIN {tabla_sec} {'WHERE estado = 1 ' * estado}{'AND' * estado} {'WHERE' * (1 - estado)} {'AND' * estado} {filtro_val};"
            else:
                sql = f"SELECT {columnas} FROM {nombre_tabla} NATURAL JOIN {tabla_sec} {'WHERE estado = 1 ' * estado};"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except db.connection.Error as error :
            err = {"title": "Error!",
                   "detalle":  str(error)}
            flash(err)
            return None

def get_tabla_raw(db, columnas, nombre_tabla, estado, order=""):
    cursor = db.connection.cursor()
    try:
        if order:
            sql = f"SELECT {columnas} from {nombre_tabla} ORDER BY {order} {'WHERE estado = 1' * estado}"
        else:
            sql = f"SELECT {columnas} from {nombre_tabla} {'WHERE estado = 1' * estado}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
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

def get_last_insert(db, nombre_tabla, col_id):
    cursor = db.connection.cursor()
    try:
        sql = f"SELECT {col_id} FROM {nombre_tabla} ORDER BY {col_id} DESC LIMIT 1;"
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def ver_child(db, id, nombre_tabla, col_id):
    cursor = db.connection.cursor()
    a = []
    columns = ''
    for i in range(1,len(col_id)):
        columns = columns + col_id[i]
    try:
        sql = f"SELECT {columns} from {nombre_tabla} WHERE {col_id[0]} = {id}"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            a.append(row[0])
        results = a
        return results
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def ver_sub_tabla(db, id, nombre_tabla, col_id):
    cursor = db.connection.cursor()
    filtro = f"{col_id} in ({id})"
    try:
        sql = f"SELECT * from {nombre_tabla} WHERE {filtro}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def ver_sub_tabla_where_not(db, id_prin, col_id_prin, id_sec, col_id_sec, nombre_tabla, id_mult=0):
    cursor = db.connection.cursor()
    valores = ""
    filtro = ""

    if len(id_sec) > 1:
        for row in id_sec:
            valores = valores + str(row) + ", "
        valores = eval(valores[0:len(valores)-2])
        if isinstance(col_id_sec, tuple):  #OJO
            for i in range(0,len(col_id_sec)):
                aux = ""
                for j in range(0,len(valores)):
                    if len(aux) == 0:
                        aux = f"{valores[j][i]}"
                    else:
                        aux = f"{aux}, {valores[j][i]}"

                if i == 0:
                    filtro_not = f"{col_id_sec[i]} not in ({aux})"
                else:
                    filtro_not = f"{filtro_not} AND {col_id_sec[i]} not in ({aux})"
        else:
            aux = ""
            for j in range(0,len(valores)):
                if len(aux) == 0:
                    aux = f"{valores[j]}"
                else:
                    aux = f"{aux}, {valores[j]}"
            filtro_not = f"{col_id_sec} not in ({aux})"

    else:
        filtro_not = f"{col_id_sec} not in ({int(id_sec[0])})"

    if id_mult == 1:
        filtro = f"AND {col_id_prin} = {id_prin}"

    try:
        sql = f"SELECT {col_id_sec} from {nombre_tabla} WHERE {filtro_not} {filtro}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def get_tabla_child(db, columnas, tabla, orden, estado, col_id, val):
    valores = ''
    for row in val:
        valores = valores + str(row) + ", "
    valores = valores[0:len(valores)-2]
    filtro = f"{col_id} in ({valores})"
    try:
        if estado:
            sql = f"SELECT {columnas} FROM {tabla} WHERE estado = 1 AND {filtro} ORDER BY {orden} asc;"
        else:
            sql = f"SELECT {columnas} FROM {tabla} WHERE {filtro} ORDER BY {orden} asc;"
        cursor = db.connection.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
        cursor.close()
        return lista
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
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
        if current_user.is_authenticated:
            user_id = session["_user_id"]
            sql = f"""SELECT actualizar, borrar, crear, leer
                    FROM permisos, tipo_user, users, tablas
                    where permisos.idtipo_user = users.idtipo_user = tipo_user.idtipo_user
                    and users.id_user = {user_id}
                    and permisos.idtabla = tablas.idtabla
                    and tablas.nombre = "{nombre_tabla}";"""
            cursor.execute(sql)
            permisos = cursor.fetchone()
        else:
            permisos = ""
        return permisos
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None

def obtener_permisos_menu(db):
    cursor = db.connection.cursor()
    try:
        if current_user.is_authenticated:
            rol = session["rol"]
            sql = f"""SELECT tablas.nombre, actualizar, borrar, crear, leer
                    FROM permisos, tipo_user, tablas
                    where tipo_user.nombre = "{rol}"
                    and permisos.idtabla = tablas.idtabla;"""
        else:
            sql = "SELECT tablas.nombre, 0, 0, 0, 0 from tablas;"
        cursor.execute(sql)
        data = cursor.fetchall()
        permisos = {}
        for row in data:
            permisos[f"{row[0]}"] = {"actualizar":row[1],
                                    "borrar":row[2],
                                    "crear":row[3],
                                    "leer":row[4]}
        session["permisos"] = permisos
    except db.connection.Error as error :
        err = {"title": "Error!",
                "detalle":  str(error)}
        flash(err)
        return None


def update(db, val, nombre_tabla, cols_act, col_id, sub=0):
    cursor = db.connection.cursor()
    cols_act = cols_act.replace(", ", " = %s, " )
    col_id = str(col_id).replace(", ", " = %s and " )
    col_id = str(col_id).replace("(", "" )
    col_id = str(col_id).replace(")", "" )
    col_id = str(col_id).replace("'", "" )

    try:
        sql = f"UPDATE {nombre_tabla} SET {cols_act} = %s WHERE {col_id} = %s;"
        cursor.execute(sql, val)
        db.connection.commit()
        if sub == 1:
            err = {"title": "Guardado!",}
            flash(err)
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None

def delete_logic(db, nombre_tabla, col_id, id, sub=0):
    cursor = db.connection.cursor()
    try:
        sql = f"UPDATE {nombre_tabla} SET estado = 0 WHERE {col_id} = {id};"
        cursor.execute(sql)
        db.connection.commit()
        if sub == 1:
            err = {"title": "Eliminado!",}
            flash(err)
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None

def delete_logic_child(db, nombre_tabla, col_id, ids):
    valores = ''
    cursor = db.connection.cursor()
    cantidad_cols = len(col_id)
    if type(ids) !=  int:
        for i in range(0,cantidad_cols):
            valores = valores + str(col_id[i]) + " = " + str(ids[i]) + " AND "
        valores = valores[0:len(valores)-5]
    else:
        valores = f"{col_id} = {ids}"

    try:
        sql = f"UPDATE {nombre_tabla} SET estado = 0 WHERE {valores};"
        cursor.execute(sql)
        db.connection.commit()
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None

def delete_fis(db, nombre_tabla, col_id, id, sub=0):
    cursor = db.connection.cursor()
    try:
        sql = f"DELETE FROM {nombre_tabla} WHERE {col_id} = {id};"
        cursor.execute(sql)
        db.connection.commit()
        if sub == 1:
            err = {"title": "Eliminado!",}
            flash(err)
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None

def delete_fis_child(db, nombre_tabla, col_id, ids):
    valores = ''
    cursor = db.connection.cursor()
    cantidad_cols = len(col_id)
    if type(ids) !=  int:
        for i in range(0,cantidad_cols):
            valores = valores + str(col_id[i]) + " = " + str(ids[i]) + " AND "
        valores = valores[0:len(valores)-5]
    else:
        valores = f"{col_id} = {ids}"

    try:
        sql = f"DELETE FROM {nombre_tabla} WHERE {valores};"
        print(sql)
        cursor.execute(sql)
        db.connection.commit()
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None