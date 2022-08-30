from itertools import islice
from openpyxl import Workbook, load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from pandas import DataFrame
import numpy as np

wb = load_workbook('p1.xlsx')
ws = wb.active
wb2 = Workbook()
ws2 = wb2.active
ws2.title = 'Prueba'
peso_evi = 0.5
peso_inst = 0.2
peso_virt = 0.2
peso_rsa = 0.1

data = ws.values
cols = next(data)[1:]
data = list(data)
idx = [r[0] for r in data]
data = (islice(r, 1, None) for r in data)
df = DataFrame(data, index=idx, columns=cols)
df.dropna(inplace=True)


def extrae_valores(fila, a, b):
    pl = int(fila[b])
    tp = int(fila[a])
    if tp==0:
        print(a,b)
        print(fila)
    else:
        porc = pl / tp * 100
        porc_tot = porc * peso_evi
    return porc, porc_tot


def guardar(wb2, ws2, df):
    for r in dataframe_to_rows(df, index=False, header=True):
        ws2.append(r)
    for cell in ws2['A'] + ws2[1]:
        cell.style = 'Pandas'
    wb2.save('p2.xlsx')


def procesos_sin_formula(df):
    porc = np.array([])
    porc_tot = np.array([])
    db = df
    for t in range(3,9,2):
        print(t)
        for fila in df.values:
            aux1, aux2 = extrae_valores(fila, t, t+1)
            porc = np.append(porc, aux1)
            porc_tot = np.append(porc_tot, aux2)
        db.insert(1, "Cálculo", porc, allow_duplicates=True)
        #df.insert((t+3), "Porcentaje", porc_tot, allow_duplicates=True)


procesos_sin_formula(df)
guardar(wb2, ws2, df)
