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
        val = nivel_escolar.nombre, nivel_escolar.exigencia, nivel_escolar.id
        update(db, val, Nivel_escolar.nombre_tabla, Nivel_escolar.cols, Nivel_escolar.col_id)
    
    def delete(db, id):
        delete_fis(Nivel_escolar.nombre_tabla, Nivel_escolar.col_id, id)

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
    
    def delete(db, id):
        delete_fis(Secciones.nombre_tabla, Secciones.col_id, id)

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
    
    def delete(db, id):
        delete_fis(Gravedad.nombre_tabla, Gravedad.col_id, id)

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
        delete_fis(Tipo_procesos.nombre_tabla, Tipo_procesos.col_id, id)

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
        delete_logic(db, Visitante.nombre_tabla, Visitante.col_id, id)

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
        delete_fis(db, Historial_ingreso.nombre_tabla, Historial_ingreso.col_id, id)

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

    def update(db, historial_ingreso):
        val = historial_ingreso.fecha, historial_ingreso.descripcion
        update(db, val, Historial_ingreso.nombre_tabla, Historial_ingreso.cols, Historial_ingreso.col_id)
    
    def delete(db, id):
        datos_sec = ver_child(db, id, Hist_ingr_det.nombre_tabla, Hist_ingr_det.col_id)
        for row in datos_sec:
            val = id, row
            delete_fis_child(db, Hist_ingr_det.nombre_tabla, Hist_ingr_det.col_id, val)

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
        delete_fis(Indicadores.nombre_tabla, Indicadores.col_id, id)

class Profesores():
    nombre_tabla = "profesores"
    orden = "nombres"
    col_id = "idprofesor"
    cols = "nombres, apellidos, documento, telefono, celular, email, domicilio"
    elim_log = 0
    
    cols_def = col_id + ", nombres, apellidos"
    tabla_col_def = ["ID", "Nombres", "Apellidos"]

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
        response = get_tabla(db, Profesores.cols_def, Profesores.tabla_col_def, Profesores.nombre_tabla, Profesores.orden, Profesores.elim_log)
        return response
    
    def nuevo(db, profesor, det):
        val = profesor.nombres, profesor.apellidos, profesor.documento, profesor.telefono, profesor.celular, profesor.email, profesor.domicilio
        nuevo(db, val, Profesores.nombre_tabla, Profesores.cols)
        Legajo.nuevo_multi(db, det)

    def ver(db, id):
        permisos = obtener_permisos(db, Profesores.nombre_tabla)
        datos = ver(db, id, Profesores.nombre_tabla, Profesores.col_id, Profesores.elim_log)
        datos_sec = Legajo.ver(db, id)
        return datos, permisos, datos_sec

    def update(db, profesor, det):
        val = profesor.nombres, profesor.apellidos, profesor.documento, profesor.telefono, profesor.celular, profesor.email, profesor.domicilio, profesor.idprofesor
        update(db, val, Profesores.nombre_tabla, Profesores.cols, Profesores.col_id)
        for row in det:
            if row[0]:
                Legajo.update(db, row)
            else:
                Legajo.nuevo_uniq(db, row)
    
    def delete(db, id):
        Legajo.delete(db, id)
        delete_fis(db, Profesores.nombre_tabla, Profesores.col_id, id)

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
        return datos_sec

    def get_to_descargar(db,id):
        datos_sec = ver(db, id, Legajo.nombre_tabla, Legajo.col_id, Legajo.elim_log)
        return datos_sec

    def nuevo_multi(db, vis_det):
        last_insert = get_last_insert(db, Profesores.nombre_tabla, Profesores.col_id)
        for row in vis_det:
            if str(row) != "b''":
                val = row, last_insert[0]
                nuevo(db, val, Legajo.nombre_tabla, Legajo.cols)

    def nuevo_uniq(db, vis_det):
        val = vis_det[1], vis_det[2]
        nuevo(db, val, Legajo.nombre_tabla, Legajo.cols)

    def update(db, leg):
        val = leg[1], leg[2], leg[0]
        update(db, val, Legajo.nombre_tabla, Legajo.cols, Legajo.col_id, 1)
    
    def delete(db, id):
        datos_sec = ver_sub_tabla(db, id, Legajo.nombre_tabla, Profesores.col_id)
        for row in datos_sec:
            val = row[0]
            delete_fis_child(db, Legajo.nombre_tabla, Legajo.col_id, val)
