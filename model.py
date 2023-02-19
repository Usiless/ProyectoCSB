from static.funciones.funciones_base_datos import *

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

    def get_tabla_raw(db):
        response = get_tabla_raw(db, Materia.cols_def, Materia.nombre_tabla, Materia.elim_log)
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
        delete_logic(db, Materia.nombre_tabla, Materia.col_id, id) #Materias

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

    def get_tabla_raw(db):
        response = get_tabla_raw(db, Nivel_escolar.cols_def, Nivel_escolar.nombre_tabla, Nivel_escolar.elim_log)
        return response
    
    def nuevo(db, nivel_escolar):
        val = nivel_escolar.nombre, nivel_escolar.exigencia
        nuevo(db, val, Nivel_escolar.nombre_tabla, Nivel_escolar.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Nivel_escolar.nombre_tabla)
        datos = ver(db, id, Nivel_escolar.nombre_tabla, Nivel_escolar.col_id, Nivel_escolar.elim_log)
        return datos, permisos

    def update(db, nivel_escolar):
        val = nivel_escolar.nombre, nivel_escolar.exigencia, nivel_escolar.id
        update(db, val, Nivel_escolar.nombre_tabla, Nivel_escolar.cols, Nivel_escolar.col_id)
    
    def delete(db, id):
        delete_fis(Nivel_escolar.nombre_tabla, Nivel_escolar.col_id, id) #Nivel Escolar

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

    def get_tabla_raw(db):
        response = get_tabla_raw(db, Secciones.cols_def, Secciones.nombre_tabla, Secciones.elim_log)
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
    
    def delete(db, id):
        delete_fis(db, Secciones.nombre_tabla, Secciones.col_id, id) #Secciones

class Tutor():
    nombre_tabla = "tutores"
    orden = "idtutor"
    col_id = "idtutor"
    cols = "nombres, apellidos, documento, celular, email, domicilio"
    elim_log = 1

    cols_def = col_id + ", concat(nombres, ' ', apellidos) as Nombre, documento"
    tabla_col_def = ["ID", "Nombre", "Documento"]

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
        delete_logic(db, Tutor.nombre_tabla, Tutor.col_id, id) #Tutores

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
    
    def get_tabla_raw(db):
        response = get_tabla_raw(db, Gravedad.cols_def, Gravedad.nombre_tabla, Gravedad.elim_log)
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
    
    def delete(db, id):
        delete_fis(db, Gravedad.nombre_tabla, Gravedad.col_id, id) #Gravedad

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
        val = tipo_proceso.descripcion, tipo_proceso.id
        update(db, val, Tipo_procesos.nombre_tabla, Tipo_procesos.cols, Tipo_procesos.col_id)
    
    def delete(db, id):
        delete_fis(db, Tipo_procesos.nombre_tabla, Tipo_procesos.col_id, id) #Tipo procesos

class Visitante():
    nombre_tabla = "visitantes"
    orden = "idvisitante"
    col_id = "idvisitante"
    cols = "nombres, apellidos, telefono"
    elim_log = 1    
    
    cols_def = col_id + ", nombres, apellidos"
    tabla_col_def = ["ID", "Nombres", "Apellidos"]

    def __init__(self, idvisitante, nombres, apellidos, telefono):
        self.id = idvisitante
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
    
    def get_tabla(db):
        response = get_tabla(db, Visitante.cols_def, Visitante.tabla_col_def, Visitante.nombre_tabla, Visitante.orden, Visitante.elim_log)
        return response

    def nuevo(db, visitante):
        val = visitante.nombres, visitante.apellidos, visitante.telefono
        nuevo(db, val, Visitante.nombre_tabla, Visitante.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Visitante.nombre_tabla)
        datos = ver(db, id, Visitante.nombre_tabla, Visitante.col_id, Visitante.elim_log)
        return datos, permisos

    def update(db, visitante):
        val = visitante.nombres, visitante.apellidos, visitante.telefono, visitante.id
        update(db, val, Visitante.nombre_tabla, Visitante.cols, Visitante.col_id)

    def delete(db, id):
        delete_logic(db, Visitante.nombre_tabla, Visitante.col_id, id) #Visitantes

class Historial_ingreso():
    nombre_tabla = "historial_de_ingresos"
    orden = "fecha, idhistorial_de_ingreso"
    col_id = "idhistorial_de_ingreso"
    cols = "fecha, descripcion"
    elim_log = 0
    
    cols_def = col_id + ",CAST(fecha AS char)"
    tabla_col_def = ["ID", "Fecha"]

    def __init__(self, idhistorial_ingreso, fecha, descripcion=""):
        self.id = idhistorial_ingreso
        self.fecha = fecha
        self.descripcion = descripcion
    
    def get_tabla(db):
        response = get_tabla(db, Historial_ingreso.cols_def, Historial_ingreso.tabla_col_def, Historial_ingreso.nombre_tabla, Historial_ingreso.orden, Historial_ingreso.elim_log)
        return response

    def nuevo(db, historial_ingreso, vis_det):
        val = historial_ingreso.fecha, historial_ingreso.descripcion
        nuevo(db, val, Historial_ingreso.nombre_tabla, Historial_ingreso.cols)
        Hist_ingr_det.nuevo(db, vis_det)

    def ver(db, id):
        permisos = obtener_permisos(db, Historial_ingreso.nombre_tabla)
        datos = ver(db, id, Historial_ingreso.nombre_tabla, Historial_ingreso.col_id, Historial_ingreso.elim_log)
        datos_sec = Hist_ingr_det.ver(db, id)
        return datos, permisos, datos_sec

    def update(db, historial_ingreso, vis_det):
        val = historial_ingreso.fecha, historial_ingreso.descripcion, historial_ingreso.id
        Hist_ingr_det.delete(db, historial_ingreso.id)
        if vis_det:
            Hist_ingr_det.nuevo(db, vis_det)
        update(db, val, Historial_ingreso.nombre_tabla, Historial_ingreso.cols, Historial_ingreso.col_id)
    
    def delete(db, id):
        Hist_ingr_det.delete(db, id)
        delete_fis(db, Historial_ingreso.nombre_tabla, Historial_ingreso.col_id, id) #Historial de Ingresos

class Hist_ingr_det():
    nombre_tabla = "visitantes_por_dia"
    orden = "idhistorial_de_ingreso, idvisitante"
    col_id = "idhistorial_de_ingreso", "idvisitante"
    cols = "idhistorial_de_ingreso, idvisitante"
    elim_log = 0

    def __init__(self, idhistorial_ingreso, idvisitante):
        self.id_his = idhistorial_ingreso
        self.id_vis = idvisitante

    def ver(db, id):
        datos_sec = ver_child(db, id, Hist_ingr_det.nombre_tabla, Hist_ingr_det.col_id)
        datos_sec = get_tabla_child(db, Visitante.cols_def, Visitante.nombre_tabla, Visitante.orden, Visitante.elim_log, Visitante.col_id, datos_sec)
        return datos_sec

    def nuevo(db, vis_det):
        last_insert = get_last_insert(db, Historial_ingreso.nombre_tabla, Historial_ingreso.col_id)
        for row in vis_det:
            val = last_insert[0], row
            nuevo(db, val, Hist_ingr_det.nombre_tabla, Hist_ingr_det.cols)
    
    def delete(db, id):
        datos_sec = ver_child(db, id, Hist_ingr_det.nombre_tabla, Hist_ingr_det.col_id)
        for row in datos_sec:
            val = id, row
            delete_fis_child(db, Hist_ingr_det.nombre_tabla, Hist_ingr_det.col_id, val) #Historial-Visitantes

class Indicadores():
    nombre_tabla = "indicadores"
    orden = "idindicadores"
    col_id = "idindicadores"
    cols = "descripción"
    elim_log = 0
    
    cols_def = col_id + ", descripción"
    tabla_col_def = ["ID", "Descripción"]

    def __init__(self, idmateria, descripcion):
        self.id = idmateria
        self.descripcion = descripcion
    
    def get_tabla(db):
        response = get_tabla(db, Indicadores.cols_def, Indicadores.tabla_col_def, Indicadores.nombre_tabla, Indicadores.orden, Indicadores.elim_log)
        return response
    
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
    
    def delete(db, id):
        delete_fis(db, Indicadores.nombre_tabla, Indicadores.col_id, id) #Indicadores

class Profesores():
    nombre_tabla = "profesores"
    orden = "nombres"
    col_id = "idprofesor"
    cols = "nombres, apellidos, documento, telefono, celular, email, domicilio"
    elim_log = 0
    
    tabla_col_def = ["ID", "Nombres", "Materias que enseña"]

    def __init__(self, idprofesor, nombres, apellidos, documento, telefono, celular, email, domicilio):
        self.idprofesor = idprofesor
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento = documento
        self.telefono = telefono
        self.celular = celular
        self.email = email
        self.domicilio = domicilio
    
    def get_tabla(db):
        sql ="""SELECT 
                profesores.idprofesor, 
                concat(nombres, ' ', apellidos) as Nombres, 
	            GROUP_CONCAT(DISTINCT CONCAT(" ", det.nombre)) AS det
            FROM materias_de_grado, profesores
            INNER JOIN 
            (SELECT materias_de_grado.idprofesor,materias.idmateria, nombre from materias, materias_de_grado where materias.idmateria = materias_de_grado.idmateria) as det
            ON det.idprofesor=profesores.idprofesor
            GROUP BY profesores.idprofesor"""
        response = get_tabla_custom_req(db, sql, Profesores.nombre_tabla, Profesores.tabla_col_def)
        return response

    #def get_tabla(db):
    #    response = get_tabla(db, Profesores.cols_def, Profesores.tabla_col_def, Profesores.nombre_tabla, Profesores.orden, Profesores.elim_log)
    #    return response
    
    def nuevo(db, profesor, det, det_2):
        val = profesor.nombres, profesor.apellidos, profesor.documento, profesor.telefono, profesor.celular, profesor.email, profesor.domicilio
        nuevo(db, val, Profesores.nombre_tabla, Profesores.cols)
        Legajo.nuevo_multi(db, det)
        Prof_materias.nuevo_multi(db, det_2)

    def ver(db, id):
        permisos = obtener_permisos(db, Profesores.nombre_tabla)
        datos = ver(db, id, Profesores.nombre_tabla, Profesores.col_id, Profesores.elim_log)
        datos_sec = Legajo.ver(db, id)
        datos_sec_2 = Prof_materias.ver(db, id)

        return datos, permisos, datos_sec, datos_sec_2

    def update(db, profesor, det, det_id, det_2, det_2_new):
        val = profesor.nombres, profesor.apellidos, profesor.documento, profesor.telefono, profesor.celular, profesor.email, profesor.domicilio, profesor.idprofesor
        update(db, val, Profesores.nombre_tabla, Profesores.cols, Profesores.col_id)
        
        if det_id:
            datos_sec = Legajo.ver_not(db, profesor.idprofesor, det_id)
            for i in datos_sec:
                Legajo.delete_one(db, i[0])

        for row in det:
            if row[0]:
                Legajo.update(db, row)
            else:
                Legajo.nuevo_uniq(db, row)

        if det_2:
            Prof_materias.update(db, det_2, profesor.idprofesor, det_2_new)

    
    def delete(db, id):
        Legajo.delete(db, id)
        delete_fis(db, Profesores.nombre_tabla, Profesores.col_id, id) #Profesores

class Legajo():
    nombre_tabla = "legajo"
    orden = "idlegajo"
    col_id = "idlegajo"
    cols = "historial_académico, idprofesor"
    elim_log = 0

    def __init__(self, id, his_acad, id_prof):
        self.idlegajo = id
        self.his_acad = his_acad
        self.id_prof = id_prof

    def ver(db, id):
        datos_sec = ver_sub_tabla(db, id, Legajo.nombre_tabla, Profesores.col_id)
        lista_id = []
        for i in datos_sec:
            lista_id.append(i[0])
        return lista_id

    def ver_not(db, id, id_det):
        datos_sec = ver_sub_tabla_where_not(db, id, Profesores.col_id, id_det, Legajo.col_id, Legajo.nombre_tabla)
        return datos_sec

    def get_to_descargar(db,id):
        datos_sec = ver(db, id, Legajo.nombre_tabla, Legajo.col_id, Legajo.elim_log)
        return datos_sec

    def nuevo_multi(db, leg):
        last_insert = get_last_insert(db, Profesores.nombre_tabla, Profesores.col_id)
        for row in leg:
            if str(row) != "b''":
                val = row, last_insert[0]
                nuevo(db, val, Legajo.nombre_tabla, Legajo.cols)

    def nuevo_uniq(db, leg):
        val = leg[1], leg[2]
        nuevo(db, val, Legajo.nombre_tabla, Legajo.cols)

    def update(db, leg):
        val = leg[1], leg[2], leg[0]
        update(db, val, Legajo.nombre_tabla, Legajo.cols, Legajo.col_id, 1)
    
    def delete(db, id):
        datos_sec = ver_sub_tabla(db, id, Legajo.nombre_tabla, Profesores.col_id)
        for row in datos_sec:
            val = row
            delete_fis_child(db, Legajo.nombre_tabla, Legajo.col_id, val)

    def delete_one(db, id):
        delete_fis_child(db, Legajo.nombre_tabla, Legajo.col_id, id) #Legajos

class Prof_materias():
    nombre_tabla = "materias_de_grado"
    orden = "idprofesor"
    col_id = "idgrado", "idmateria", "idprofesor"
    cols = "estado"
    elim_log = 1

    cols_def = f" {cols}, {col_id[0]}, {col_id[1]}, {col_id[2]}"

    def __init__(self, idgrado, idmateria, id_prof, estado):
        self.idgrado = idgrado
        self.idmateria = idmateria
        self.id_prof = id_prof
        self.estado = estado

    def ver(db, id):
        datos_sec = ver_sub_tabla(db, id, Prof_materias.nombre_tabla, Profesores.col_id)
        return datos_sec

    def ver_not(db, id, id_det):
        datos_sec = ver_sub_tabla_where_not(db, id, Profesores.col_id, id_det, Prof_materias.col_id, Prof_materias.nombre_tabla)
        return datos_sec

    def update(db, prof_mat, id_prof, prof_mat_new):
        Prof_materias.delete(db, id_prof)
        control = 0
        for row in prof_mat:
            val = eval(f"1, {row}")
            update(db, val, Prof_materias.nombre_tabla, Prof_materias.cols, Prof_materias.col_id)
        for det in prof_mat_new:
            aux = ""
            for i in det:
                if i:
                    aux = aux + f"{int(i)}, {id_prof}"
                aux = aux + str(id_prof)
            aux = eval(aux[0:len(aux)-2])
            for row in prof_mat:
                val = eval(f"1, {row}")
                if aux == val:
                    control+=1
            print(det)
            print(aux)
            #if control == 0:
                #Prof_materias.nuevo_multi(db,aux,id_prof)

    def nuevo_multi(db, det, id_prof=0):
        if id_prof == 0:
            last_insert = get_last_insert(db, Profesores.nombre_tabla, Profesores.col_id)
            id_prin = last_insert[0]
            for row in det:
                val = int(row[0]), int(row[1]), int(row[2]), id_prin
                print(row)
                print(val)
                print(Prof_materias.cols_def)
                nuevo(db, val, Prof_materias.nombre_tabla, Prof_materias.cols_def)
        else:
            nuevo(db, det, Prof_materias.nombre_tabla, Prof_materias.cols_def)
            
    def delete(db, id):
        datos_sec = ver_sub_tabla(db, id, Prof_materias.nombre_tabla, Profesores.col_id)
        for row in datos_sec:
            val = row[0], row[1], row[2]
            delete_logic_child(db, Prof_materias.nombre_tabla, Prof_materias.col_id, val) #Profesores-Materias

class Grados():
    nombre_tabla = "grados"
    orden = "grado"
    col_id = "idgrado"
    cols = "grado, idseccion, idnivel_escolar"
    elim_log = 1


    cols_def = col_id + ", grado," + Secciones.nombre_tabla + ".nombre"
    tabla_col_def = ["ID", "Grado", "Sección"]

    def __init__(self, idgrado, grado, idseccion, idnivel_escolar):
        self.id = idgrado
        self.grado = grado
        self.idseccion = idseccion
        self.idnivel_escolar = idnivel_escolar

    def get_tabla(db):
        tablas_sec = Secciones.nombre_tabla
        response = get_tabla_compleja(db, Grados.cols_def, Grados.tabla_col_def, Grados.nombre_tabla, tablas_sec, Grados.orden, Grados.elim_log)
        return response

    def get_tabla_raw(db):
        tablas_sec = Secciones.nombre_tabla
        response = get_tabla_compleja_raw(db, Grados.cols_def, Grados.nombre_tabla, tablas_sec, Grados.elim_log)
        return response
    
    def nuevo(db, grado):
        val = grado.grado, grado.idseccion, grado.idnivel_escolar
        nuevo(db, val, Grados.nombre_tabla, Grados.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Grados.nombre_tabla)
        datos = ver(db, id, Grados.nombre_tabla, Grados.col_id, Grados.elim_log)
        return datos, permisos

    def update(db, grado):
        val = grado.grado, grado.idseccion, grado.idnivel_escolar, grado.id
        update(db, val, Grados.nombre_tabla, Grados.cols, Grados.col_id)

    def delete(db, id):
        delete_logic(db, Grados.nombre_tabla, Grados.col_id, id) #Grados

class Horario():
    nombre_tabla = "horario"
    orden = "dia, inicio"
    col_id = "idhorario"
    cols = "dia, idgrado, idmateria, idprofesor, inicio, fin, turno, año, estado"
    elim_log = 1


    cols_def = f"{col_id}, dia, CONCAT(TIME_FORMAT(inicio, '%H:%i'), ' - ', TIME_FORMAT(fin, '%H:%i')) AS Hora, CONCAT( {Materia.nombre_tabla}.nombre, ' - ',{Profesores.nombre_tabla}.nombres, ' ', {Profesores.nombre_tabla}.apellidos) AS 'Materia - Docente'"
    tabla_col_def = ["ID","Día","Inicio - Fin", "Materia-Docente"]
    recreo = "'','',CONCAT(TIME_FORMAT(horario_recreo_manhana, '%H:%i'), ' - ', TIME_FORMAT(ADDTIME(horario_recreo_manhana,'00:20:00'), '%H:%i')), 'Recreo' " + f"FROM {Nivel_escolar.nombre_tabla} natural join {Grados.nombre_tabla} where {Grados.nombre_tabla}.{Grados.col_id} = 1"

    #def __init__(self, idgrado, grado, idseccion, idnivel_escolar):
    #    self.id = idgrado
    #    self.grado = grado
    #    self.idseccion = idseccion
    #    self.idnivel_escolar = idnivel_escolar

    def get_tabla(db):
        response = []
        grados = Grados.get_tabla_raw(db)
        for grado in grados:
            data = []
            for i in range(1,6):
                sql = f"""(SELECT idhorario, idgrado, dia, CONCAT(TIME_FORMAT(inicio, '%H:%i'), ' - ', TIME_FORMAT(fin, '%H:%i')) AS Hora, 
                        CONCAT( materias.nombre, ' - ',profesores.nombres, ' ', profesores.apellidos) AS 'Materia - Docente' 
                        FROM horario  NATURAL JOIN grados NATURAL JOIN materias NATURAL JOIN profesores WHERE estado = 1 and dia = {i} 
                        and idgrado = {grado[0]} ORDER BY dia, inicio) 
                        UNION 
                        (SELECT '','','',
                        CONCAT(TIME_FORMAT(horario_recreo_manhana, '%H:%i'), ' - ', TIME_FORMAT(ADDTIME(horario_recreo_manhana,'00:20:00'), '%H:%i')),
                        'Recreo' FROM nivel_escolar natural join grados where grados.idgrado = 1) 
                        ORDER BY hora;"""
                a = get_tabla_custom_req_raw(db, sql, Horario.nombre_tabla)
                data.append(a)
            response.append(data)
        return response
    
    def nuevo(db, grado):
        val = grado.grado, grado.idseccion, grado.idnivel_escolar
        nuevo(db, val, Grados.nombre_tabla, Grados.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Grados.nombre_tabla)
        datos = ver(db, id, Grados.nombre_tabla, Grados.col_id, Grados.elim_log)
        return datos, permisos

    def update(db, grado):
        val = grado.grado, grado.idseccion, grado.idnivel_escolar, grado.id
        update(db, val, Grados.nombre_tabla, Grados.cols, Grados.col_id)

    def delete(db, id):
        delete_logic(db, Grados.nombre_tabla, Grados.col_id, id) #Horario de clases

class Doctores():
    nombre_tabla = "doctores"
    orden = "nombres"
    col_id = "iddoctor"
    cols = "nombres, apellidos, reg_prof"
    elim_log = 0

    cols_def = col_id + ", concat(nombres, ' ', apellidos), reg_prof"
    tabla_col_def = ["ID", "Nombre", "Registro Profesional"]

    def __init__(self, iddoctor, nombre, apellido, reg_prof):
        self.id = iddoctor
        self.nombre = nombre
        self.apellido = apellido
        self.reg_prof = reg_prof

    def get_tabla(db):
        response = get_tabla(db, Doctores.cols_def, Doctores.tabla_col_def, Doctores.nombre_tabla, Doctores.orden, Doctores.elim_log)
        return response

    def get_tabla_raw(db):
        response = get_tabla_raw(db, Doctores.cols_def, Doctores.nombre_tabla, Doctores.elim_log)
        return response
    
    def nuevo(db, doctor):
        val = doctor.nombre, doctor.apellido, doctor.reg_prof
        nuevo(db, val, Doctores.nombre_tabla, Doctores.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Doctores.nombre_tabla)
        datos = ver(db, id, Doctores.nombre_tabla, Doctores.col_id, Doctores.elim_log)
        return datos, permisos

    def update(db, doctor):
        val = doctor.nombre, doctor.apellido, doctor.reg_prof, doctor.id
        update(db, val, Doctores.nombre_tabla, Doctores.cols, Doctores.col_id)

    def delete(db, id):
        delete_fis(db, Doctores.nombre_tabla, Doctores.col_id, id) #Doctores

class Afecciones():
    nombre_tabla = "afecciones"
    orden = "idafeccion"
    col_id = "idafeccion"
    cols = "descrpcion"
    elim_log = 0

    cols_def = col_id + ", descrpcion"
    tabla_col_def = ["ID", "Descipción"]

    def __init__(self, idafeccion, descrip):
        self.id = idafeccion
        self.descrip = descrip

    def get_tabla(db):
        response = get_tabla(db, Afecciones.cols_def, Afecciones.tabla_col_def, Afecciones.nombre_tabla, Afecciones.orden, Afecciones.elim_log)
        return response

    def get_tabla_raw(db):
        response = get_tabla_raw(db, Afecciones.cols_def, Afecciones.nombre_tabla, Afecciones.elim_log)
        return response
    
    def nuevo(db, afeccion):
        val = afeccion.descrip
        nuevo(db, val, Afecciones.nombre_tabla, Afecciones.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Afecciones.nombre_tabla)
        datos = ver(db, id, Afecciones.nombre_tabla, Afecciones.col_id, Afecciones.elim_log)
        return datos, permisos

    def update(db, afeccion):
        val = afeccion.descrip, afeccion.id
        update(db, val, Afecciones.nombre_tabla, Afecciones.cols, Afecciones.col_id)
    
    def delete(db, id):
        delete_fis(db, Afecciones.nombre_tabla, Afecciones.col_id, id) #Afecciones

class Relacion():
    nombre_tabla = "relacion"
    orden = "idalumno"
    col_id = "idtutor", "idalumno"
    cols = "idtutor, idalumno"
    elim_log = 0

    def __init__(self, idtutor, idalumno):
        self.idtutor = idtutor
        self.idalumno = idalumno

    def ver(db, id):
        data = []
        aux = ver_sub_tabla(db, id, Relacion.nombre_tabla, Alumnos.col_id)
        for row in aux:
            data.append(Tutor.ver(db,row[0])[0])
        return data

    def ver_not(db, id, id_det):
        datos_sec = ver_sub_tabla_where_not(db, id, Tutor.col_id, id_det, Relacion.col_id, Relacion.nombre_tabla,1)
        return datos_sec

    def nuevo_multi(db, datos_sec):
        last_insert = get_last_insert(db, Alumnos.nombre_tabla, Alumnos.col_id)
        for row in datos_sec:
            if row != "":
                val = row, last_insert[0]
                nuevo(db, val, Relacion.nombre_tabla, Relacion.cols)
    
    def upd_multi(db, datos_sec, id_prin):
        for row in datos_sec:
            if row:
                val = row[0], id_prin
                nuevo(db, val, Relacion.nombre_tabla, Relacion.cols)            
    
    def delete(db, id):
        datos_sec = ver_sub_tabla(db, id, Relacion.nombre_tabla, Alumnos.col_id)
        for row in datos_sec:
            val = row[0], row[1]
            delete_fis_child(db, Relacion.nombre_tabla, Relacion.col_id, val) #Tutores-Alumnos

class Alumnos():
    nombre_tabla = "alumnos"
    orden = "Grado, nombres, apellidos"
    col_id = "idalumno"
    cols = "nombres, apellidos, documento, celular, email, idgrado, fecha_nacimiento"
    elim_log = 1
    
    cols_def = f"{col_id}, concat(nombres, ' ', apellidos) as Nombre, concat({Grados.nombre_tabla}.grado,' - ', {Secciones.nombre_tabla}.nombre) as Grado"
    "grados,secciones"
    tabla_col_def = ["ID", "Nombre", "Grado"]

    def __init__(self, idalumno, nombres, apellidos, documento, celular, email, idgrado, fecha_nac):
        self.idalumno = idalumno
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento = documento
        self.celular = celular
        self.email = email
        self.idgrado = idgrado
        self.fecha_nac = fecha_nac
    
    def get_tabla(db):
        tablas_sec = Grados.nombre_tabla, Secciones.nombre_tabla
        response = get_tabla_compleja(db, Alumnos.cols_def, Alumnos.tabla_col_def, Alumnos.nombre_tabla, tablas_sec, Alumnos.orden, Alumnos.elim_log)
        return response
    
    def nuevo(db, alumno, det_1, det_2, det_2_sec):
        val = alumno.nombres, alumno.apellidos, alumno.documento, alumno.celular, alumno.email, alumno.idgrado, alumno.fecha_nac
        nuevo(db, val, Alumnos.nombre_tabla, Alumnos.cols)
        Relacion.nuevo_multi(db, det_1)
        Ficha.nuevo(db, det_2, det_2_sec)

    def ver(db, id):
        permisos = obtener_permisos(db, Alumnos.nombre_tabla)
        datos = ver(db, id, Alumnos.nombre_tabla, Alumnos.col_id, Alumnos.elim_log)
        datos_det = Relacion.ver(db,id)
        datos_det_2 = Ficha.ver_alum(db, id)
        return datos, permisos, datos_det, datos_det_2

    def update(db, alumno, det_1, det_2, det_2_sec):
        val = alumno.nombres, alumno.apellidos, alumno.documento, alumno.celular, alumno.email, alumno.idgrado, alumno.fecha_nac, alumno.idalumno
        update(db, val, Alumnos.nombre_tabla, Alumnos.cols, Alumnos.col_id)
        
        if det_1:
            Relacion.delete(db, alumno.idalumno)
            Relacion.upd_multi(db, det_1, alumno.idalumno)
        
        Ficha.nuevo(db, det_2, det_2_sec, alumno.idalumno)
    
    def delete(db, id):
        #Relacion.delete(db, id)
        #Ficha.delete_alumn(db, id)
        delete_logic(db, Alumnos.nombre_tabla, Alumnos.col_id, id) #Alumnos

class Historial_obs():
    nombre_tabla = "historial_observaciones"
    orden = "fecha"
    col_id = "idhistorial_observaciones"
    cols = "fecha, descripcion"
    elim_log = 0
    
    tabla_col_def = ["ID", "Fecha", "Involucrados"]

    def __init__(self, id_hist_obs, fecha, descripcion=""):
        self.id = id_hist_obs
        self.fecha = fecha
        self.descripcion = descripcion
    
    def get_tabla(db):
        sql ="""SELECT 
                    historial_observaciones.idhistorial_observaciones,
                    CAST(historial_observaciones.fecha AS char), 
	                GROUP_CONCAT(CONCAT(" ", part.nombres, " ", part.apellidos)) AS alumnos
                FROM participantes, historial_observaciones
                INNER JOIN 
                (SELECT idhistorial_observaciones, participantes.idalumno, alumnos.nombres, alumnos.apellidos 
                from alumnos, participantes where alumnos.idalumno = participantes.idalumno) as part
                ON part.idhistorial_observaciones=historial_observaciones.idhistorial_observaciones
                GROUP BY historial_observaciones.idhistorial_observaciones"""
        response = get_tabla_custom_req(db, sql, Historial_obs.nombre_tabla, Historial_obs.tabla_col_def)
        return response

    def nuevo(db, obs, det):
        val = obs.fecha, obs.descripcion
        nuevo(db, val, Historial_obs.nombre_tabla, Historial_obs.cols)
        Hist_obs_det.nuevo(db, det)

    def ver(db, id):
        permisos = obtener_permisos(db, Historial_obs.nombre_tabla)
        datos = ver(db, id, Historial_obs.nombre_tabla, Historial_obs.col_id, Historial_obs.elim_log)
        datos_sec = Hist_obs_det.ver(db, id)
        return datos, permisos, datos_sec

    def update(db, obs, det):
        val = obs.fecha, obs.descripcion, obs.id
        Hist_obs_det.delete(db, obs.id)
        if det:
            Hist_obs_det.upd_multi(db, det, obs.id)
        update(db, val, Historial_obs.nombre_tabla, Historial_obs.cols, Historial_obs.col_id)
    
    def delete(db, id):
        Hist_obs_det.delete(db, id)
        delete_fis(db, Historial_obs.nombre_tabla, Historial_obs.col_id, id) #Historial de observaciones

class Hist_obs_det():
    nombre_tabla = "participantes"
    orden = "idhistorial_observaciones, idalumno"
    col_id = "idhistorial_observaciones", "idalumno"
    cols = "idhistorial_observaciones, idalumno, idgravedad, descripcion"
    elim_log = 0

    cols_def = "idhistorial_observaciones, idalumno, nombres, apellidos, idgravedad, descripcion"

    def __init__(self, id_obs, id_alu, idgravedad, descripcion):
        self.id_obs = id_obs
        self.id_alu = id_alu
        self.idgravedad = idgravedad
        self.descripcion = descripcion

    def ver(db, id):
        tablas_sec = Alumnos.nombre_tabla
        response = get_tabla_compleja_raw(db, Hist_obs_det.cols_def, Hist_obs_det.nombre_tabla, tablas_sec, Hist_obs_det.elim_log, f"idhistorial_observaciones in ({id})")
        return response

    def nuevo(db, vis_det):
        last_insert = get_last_insert(db, Historial_obs.nombre_tabla, Historial_obs.col_id)
        for row in vis_det:
            print(vis_det)
            val = last_insert[0], row[0], row[1], row[2]
            nuevo(db, val, Hist_obs_det.nombre_tabla, Hist_obs_det.cols)

    def upd_multi(db, datos_sec, id_prin):
        for row in datos_sec:
            if row[0]:
                val = id_prin, row[0], row[1], row[2]
                nuevo(db, val, Hist_obs_det.nombre_tabla, Hist_obs_det.cols)
    
    def delete(db, id):
        datos_sec = ver_child(db, id, Hist_obs_det.nombre_tabla, Hist_obs_det.col_id)
        for row in datos_sec:
            val = id, row
            delete_fis_child(db, Hist_obs_det.nombre_tabla, Hist_obs_det.col_id, val) #Observaciones-Alumnos

class Ficha():
    nombre_tabla = "fichas_medicas"
    orden = "fecha"
    col_id = "idficha_medica"
    cols = "fecha, aptitud, iddoctor, idalumno"
    elim_log = 0
    
    cols_def = f"{col_id}, fecha, concat({Alumnos.nombre_tabla}.nombres,' ', {Alumnos.nombre_tabla}.apellidos) as Alumno, aptitud"
    tabla_col_def = ["ID", "Fecha", "Estudiante", "Aptitud"]

    def __init__(self, idficha_medica, fecha, aptitud, iddoctor, idalumno=0):
        self.idficha_medica = idficha_medica
        self.fecha = fecha
        self.aptitud = aptitud
        self.iddoctor = iddoctor
        self.idalumno = idalumno

    def ver(db, id):
        permisos = obtener_permisos(db, Ficha.nombre_tabla)
        datos = ver(db, id, Ficha.nombre_tabla, Ficha.col_id, Ficha.elim_log)
        datos_det = Obs_med.ver(db,datos[0])
        return datos, permisos, datos_det

    def ver_alum(db, id):
        ficha_medica = ver_sub_tabla(db, id, Ficha.nombre_tabla, Alumnos.col_id)

        return ficha_medica

    def get_tabla(db):
        tablas_sec = Alumnos.nombre_tabla
        response = get_tabla_compleja(db, Ficha.cols_def, Ficha.tabla_col_def, Ficha.nombre_tabla, tablas_sec, Ficha.orden, Ficha.elim_log)
        return response

    def ver_not(db, id, id_det):
        datos_sec = ver_sub_tabla_where_not(db, id, Ficha.col_id, id_det, Ficha.col_id, Ficha.nombre_tabla)
        return datos_sec

    def nuevo(db, ficha, det, id_prin=0):
        if not id_prin:
            last_insert = get_last_insert(db, Alumnos.nombre_tabla, Alumnos.col_id)
            id_prin = last_insert[0]
        val = ficha.fecha, ficha.aptitud, ficha.iddoctor, id_prin
        if ficha.fecha and ficha.aptitud and ficha.iddoctor:
            nuevo(db, val, Ficha.nombre_tabla, Ficha.cols)
            if list(det)[0][0]:
                Obs_med.nuevo_multi(db, det)

    def update(db, ficha, det_1):
        val = ficha.fecha, ficha.aptitud, ficha.iddoctor, ficha.idalumno, ficha.idficha_medica
        update(db, val, Ficha.nombre_tabla, Ficha.cols, Ficha.col_id)
        
        if det_1:
            Obs_med.delete(db, ficha.idficha_medica)
            Obs_med.upd_multi(db, det_1, ficha.idficha_medica)
    
    def delete(db, id):
        Obs_med.delete(db, id)
        delete_fis(db, Ficha.nombre_tabla, Ficha.col_id, id)

    def delete_alumn(db, id_alumn):
        ficha_medica = ver_sub_tabla(db, id_alumn, Ficha.nombre_tabla, Alumnos.col_id)
        if ficha_medica:
            for row in ficha_medica:
                Obs_med.delete(db, row[0])
                delete_fis(db, Ficha.nombre_tabla, Ficha.col_id, row[0], 1) #Ficha Médica

class Obs_med():
    nombre_tabla = "observaciones"
    orden = "idficha_medica"
    col_id = "idafeccion", "idficha_medica"
    cols = "idafeccion, idficha_medica, recomendacion"
    elim_log = 0

    def __init__(self, idafeccion, idficha_medica, recom):
        self.idafeccion = idafeccion
        self.idficha_medica = idficha_medica
        self.recom = recom

    def ver(db, id):
        data = ver_sub_tabla(db, id, Obs_med.nombre_tabla, Ficha.col_id)
        return data

    def ver_not(db, id, id_det):
        datos_sec = ver_sub_tabla_where_not(db, id, Obs_med.col_id, id_det, Obs_med.col_id, Obs_med.nombre_tabla)
        return datos_sec

    def nuevo_multi(db, datos_sec):
        last_insert = get_last_insert(db, Ficha.nombre_tabla, Ficha.col_id)
        for row in datos_sec:
            val = row[0], last_insert[0], row[1]
            nuevo(db, val, Obs_med.nombre_tabla, Obs_med.cols)
    
    def upd_multi(db, datos_sec, id_prin):
        for row in datos_sec:
            if row[0]:
                val = row[0], id_prin, row[1]
                nuevo(db, val, Obs_med.nombre_tabla, Obs_med.cols)

    def delete(db, id):
        datos_sec = ver_sub_tabla(db, id, Obs_med.nombre_tabla, Ficha.col_id)
        for row in datos_sec:
            val = row[0], row[1]
            delete_fis_child(db, Obs_med.nombre_tabla, Obs_med.col_id, val) #Afecciones-Ficha médica

class Noticias():
    nombre_tabla = "noticias"
    orden = "fecha DESC"
    col_id = "idnoticias"
    cols = "fecha, titulo, encabezado, descripcion, autor, user_id_user"
    elim_log = 0

    cols_def = col_id + ", titulo, fecha, encabezado"
    tabla_col_def = ["ID", "Titulo", "Fecha", "Enzabezado"]

    def __init__(self, idnoticias, fecha, titulo, encabezado, descripcion, autor, user_id_user):
        self.idnoticias = idnoticias
        self.fecha = fecha
        self.titulo = titulo
        self.encabezado = encabezado
        self.descripcion = descripcion
        self.autor = autor
        self.user_id_user = user_id_user

    def get_tabla(db):
        response = get_tabla(db, Noticias.cols_def, Noticias.tabla_col_def, Noticias.nombre_tabla, Noticias.orden, Noticias.elim_log)
        return response

    def get_tabla_raw(db):
        permisos = obtener_permisos(db, Noticias.nombre_tabla)
        response = get_tabla_raw(db, Noticias.cols_def, Noticias.nombre_tabla, Noticias.elim_log, Noticias.orden)
        return response, permisos
    
    def nuevo(db, noticia):
        val = noticia.fecha, noticia.titulo, noticia.encabezado, noticia.descripcion, noticia.autor, noticia.user_id_user
        nuevo(db, val, Noticias.nombre_tabla, Noticias.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Noticias.nombre_tabla)
        datos = ver(db, id, Noticias.nombre_tabla, Noticias.col_id, Noticias.elim_log)
        return datos, permisos

    def update(db, noticia):
        val = noticia.fecha, noticia.titulo, noticia.encabezado, noticia.descripcion, noticia.autor, noticia.user_id_user, noticia.idnoticias
        update(db, val, Noticias.nombre_tabla, Noticias.cols, Noticias.col_id)

    def delete(db, id):
        delete_fis(db, Noticias.nombre_tabla, Noticias.col_id, id) #Noticia

class User_local():
    nombre_tabla = "users"
    orden = "username"
    col_id = "id_user"
    cols = "username, fullname, email, idtipo_user"
    elim_log = 1

    cols_def = col_id + ", username, fullname, email"
    tabla_col_def = ["ID", "Nombre de Usuario", "Nombre real", "Email"]

    def update_rol(db, id, id_tipo):
        val = id_tipo, id
        update(db, val, User_local.nombre_tabla, "idtipo_user", User_local.col_id)
    
    def ver_users(db):
        data = get_tabla(db, User_local.cols_def, User_local.tabla_col_def, User_local.nombre_tabla, User_local.orden, User_local.elim_log)
        return data

    def nuevo(db, username, fullname, email, idtipo_user):
        val = username, fullname, email, idtipo_user
        nuevo(db, val, User_local.nombre_tabla, User_local.cols) #User-clase custom

class Personal():
    nombre_tabla = "personal"
    orden = "nombres"
    col_id = "idpersonal"
    cols = "nombres, apellidos, documento, celular, email"
    elim_log = 1

    cols_def = col_id + ", nombres, apellidos, documento"
    tabla_col_def = ["ID", "Nombre", "Apellido", "Documento"]

    def __init__(self, idpersonal, nombre, apellido, documento, celular, email):
        self.id = idpersonal
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.celular = celular
        self.email = email

    def get_tabla(db):
        response = get_tabla(db, Personal.cols_def, Personal.tabla_col_def, Personal.nombre_tabla, Personal.orden, Personal.elim_log)
        return response
    
    def nuevo(db, personal):
        val = personal.nombre, personal.apellido, personal.documento, personal.celular, personal.email
        nuevo(db, val, Personal.nombre_tabla, Personal.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Personal.nombre_tabla)
        datos = ver(db, id, Personal.nombre_tabla, Personal.col_id, Personal.elim_log)
        return datos, permisos

    def update(db, personal):
        val = personal.nombre, personal.apellido, personal.documento, personal.celular, personal.email, personal.id
        update(db, val, Personal.nombre_tabla, Personal.cols, Personal.col_id)

    def delete(db, id):
        delete_logic(db, Personal.nombre_tabla, Personal.col_id, id) #Personal

class Roles():
    nombre_tabla = "tipo_user"
    orden = "nombre"
    col_id = "idtipo_user"
    cols = "nombre, descripción"
    elim_log = 1

    cols_def = col_id + ", grado," + Secciones.nombre_tabla + ".nombre"
    tabla_col_def = ["ID", "Grado", "Sección"]

    def __init__(self, idgrado, grado, idseccion, idnivel_escolar):
        self.id = idgrado
        self.grado = grado
        self.idseccion = idseccion
        self.idnivel_escolar = idnivel_escolar

    def get_tabla(db):
        tablas_sec = Secciones.nombre_tabla
        response = get_tabla_compleja(db, Grados.cols_def, Grados.tabla_col_def, Grados.nombre_tabla, tablas_sec, Grados.orden, Grados.elim_log)
        return response

    def get_tabla_raw(db):
        tablas_sec = Secciones.nombre_tabla
        response = get_tabla_compleja_raw(db, Grados.cols_def, Grados.nombre_tabla, tablas_sec, Grados.elim_log)
        return response
    
    def nuevo(db, grado):
        val = grado.grado, grado.idseccion, grado.idnivel_escolar
        nuevo(db, val, Grados.nombre_tabla, Grados.cols)

    def ver(db, id):
        permisos = obtener_permisos(db, Grados.nombre_tabla)
        datos = ver(db, id, Grados.nombre_tabla, Grados.col_id, Grados.elim_log)
        return datos, permisos

    def update(db, grado):
        val = grado.grado, grado.idseccion, grado.idnivel_escolar, grado.id
        update(db, val, Grados.nombre_tabla, Grados.cols, Grados.col_id)

    def delete(db, id):
        delete_logic(db, Grados.nombre_tabla, Grados.col_id, id) #Grados

class Rol():
    nombre_tabla = "tipo_user"
    orden = "nombre"
    col_id = "idtipo_user"
    cols = "nombre, descripcion"
    elim_log = 0
    
    cols_def = col_id + ", nombre"
    tabla_col_def = ["ID", "Nombre"]

    def __init__(self, idrol, nombre, descripcion=""):
        self.id = idrol
        self.nombre = nombre
        self.descripcion = descripcion
    
    def get_tabla(db):
        response = get_tabla(db, Rol.cols_def, Rol.tabla_col_def, Rol.nombre_tabla, Rol.orden, Rol.elim_log)
        return response

    def nuevo(db, rol, det):
        val = rol.nombre, rol.descripcion
        nuevo(db, val, Rol.nombre_tabla, Rol.cols)
        Permisos.nuevo_multi(db, det)

    def ver(db, id_tipo_usr):
        permisos = obtener_permisos(db, Rol.nombre_tabla)
        datos = ver(db, id_tipo_usr, Rol.nombre_tabla, Rol.col_id, Rol.elim_log)
        datos_sec = Permisos.ver(db, id_tipo_usr)
        return datos, datos_sec, permisos

    def update(db, rol, det):
        val = rol.nombre, rol.descripcion, rol.id
        print(det)
        Permisos.delete(db, rol.id)
        if det:
            Permisos.upd_multi(db, det, rol.id)
        update(db, val, Rol.nombre_tabla, Rol.cols, Rol.col_id)
    
    def delete(db, id_tipo_usr):
        Permisos.delete(db, id_tipo_usr)
        delete_fis(db, Rol.nombre_tabla, Rol.col_id, id_tipo_usr) #Roles

class Permisos():
    nombre_tabla = "permisos"
    orden = "idtabla"
    col_id = "idtipo_user", "idtabla"
    cols = "idtipo_user, idtabla, crear, leer, actualizar, borrar"
    elim_log = 0

    def __init__(self, idtipo_user, idtabla, crear=0,leer=0,actualizar=0,borrar=0):
        self.idtipo_user = idtipo_user
        self.idtabla = idtabla
        self.crear = crear
        self.leer = leer
        self.actualizar = actualizar
        self.borrar = borrar

    def ver(db, id_tipo_usr):
        tablas_sec = "tablas"
        sql = """(SELECT 0,table_name,0,0,0,0 FROM information_schema.tables 
                WHERE table_schema = 'csb_prov' and table_name not in (select nombre from tablas));"""
        nuevas_tab = get_tabla_custom_req_raw(db, sql, "tablas")
        for i in nuevas_tab:
            nuevo(db,i[1],"tablas","nombre")
        if id_tipo_usr:
            filtro = f" idtipo_user='{id_tipo_usr}'"
        else:
            filtro = "idtipo_user='0'"
        sql = f"""(SELECT idtabla,nombre,0,0,0,0 FROM tablas 
                WHERE idtabla not in (select idtabla from permisos where idtipo_user='{id_tipo_usr}'));"""
        tablas_sin_per = get_tabla_custom_req_raw(db, sql, "tablas")
        perm_act = get_tabla_compleja_raw(db, "idtabla, tablas.nombre, crear, leer, actualizar, borrar ", Permisos.nombre_tabla, tablas_sec, Permisos.elim_log, f"{filtro}")
        if id_tipo_usr:
            response = tablas_sin_per + perm_act
        else:
            response = tablas_sin_per
        return response

    #def ver_not(db, id, id_det):
    #    datos_sec = ver_sub_tabla_where_not(db, id, Tutor.col_id, id_det, Permisos.col_id, Relacion.nombre_tabla,1)
    #    return datos_sec

    def nuevo_multi(db, datos_sec):
        last_insert = get_last_insert(db, Rol.nombre_tabla, Rol.col_id)
        for row in datos_sec:
            val = last_insert[0],row[0],row[1],row[2],row[3],row[4]
            nuevo(db, val, Permisos.nombre_tabla, Permisos.cols)
    
    def upd_multi(db, datos_sec, id_prin):
        for row in datos_sec:
            val = id_prin,row[0],row[1],row[2],row[3],row[4]
            print(val)
            nuevo(db, val, Permisos.nombre_tabla, Permisos.cols)            
    
    def delete(db, id_tipo_usr):
        datos_sec = ver_sub_tabla(db, id_tipo_usr, Permisos.nombre_tabla, Rol.col_id)
        for row in datos_sec:
            if row[0] !=0:
                val = row[0], row[1]
                delete_fis_child(db, Permisos.nombre_tabla, Permisos.col_id, val) #Permisos
