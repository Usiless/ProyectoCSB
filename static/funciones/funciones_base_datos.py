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

def update(db, val, nombre_tabla, cols_act, col_id, sub=0):
    cursor = db.connection.cursor()
    cols_act = cols_act.replace(", ", " = %s, " )

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
        cursor.execute(sql)
        db.connection.commit()
        return None
    except db.connection.Error as error :
        err = {"title": "Cambio en la base fallido!",
                "detalle":  str(error)}
        flash(err)
        db.connection.rollback()
        return None