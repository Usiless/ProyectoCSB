import io
from model import Legajo
import base64
from PIL import Image

def convierte_64_a_img(db, value):
    datos_sec = Legajo.get_to_descargar(db, value)
    image = datos_sec[1]
    img = str(image)
    img = img[2:len(img)-1]
    binary_data = base64.b64decode(image)
  
    image = Image.open(io.BytesIO(binary_data))
    filetype = (image.format).lower()
    src = f"data:image/{filetype};base64,{img}"
    html = f'<img src="{src}">'
    return html

def convierte_img_a_64_multi(legajo):
    legajo_raw = []
    for i in legajo:
        a = i[1].read()
        recons = [i[0], base64.b64encode(a), i[2]]
        legajo_raw.append(recons)
    return legajo_raw

def convierte_img_a_64(legajo):
    legajo_raw = []
    for i in legajo:
        a = i.read()
        legajo_raw.append(base64.b64encode(a))
    return legajo_raw

def limpia_sub_tabla_uniq(detalle_raw):
    detalle = []
    for row in detalle_raw:
        if row!="":
            detalle.append(row)
    return detalle

def limpia_sub_tabla_multi_arch(detalle_raw):
    detalle = []
    for row in detalle_raw:
        if str(row[1])!="<FileStorage: '' ('application/octet-stream')>":
            detalle.append(row)
    return detalle


def combina_varios(grados, estados, materias):
    mat_grad_prof = []
    for i in range(0,len(grados)):
        if grados[i] != '':
            a = estados[i]
            if a=='on':
                a = 1
            else:
                a = 0
            mat_grad_prof.append([grados[i], materias[i], a])
    return mat_grad_prof