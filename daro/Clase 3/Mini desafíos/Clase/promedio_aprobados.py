import pandas as pan
import numpy as np

try:
    data = pan.read_excel("Datos.xlsx")
    approved = data[data['Quimica'] >= 4]
    scores_q = np.mean(np.array(approved['Quimica']))
    scores_f = np.mean(np.array(approved['Fisica']))
    scores_m = np.mean(np.array(approved['Matematica']))
    total_average = np.mean(np.array([scores_q, scores_f, scores_m]))
    print(f'El promedio general es {total_average:.2f}')
except:
    print('No se pudo acceder a la información.')
