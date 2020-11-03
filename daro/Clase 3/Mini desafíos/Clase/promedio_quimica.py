import pandas as pan
import numpy as np

try:
    data = pan.read_excel("Datos.xlsx", )
    data_dict = data.to_dict("list")
    scores = np.array(data_dict['Quimica'])
    average = np.mean(scores)
    print(f'El promedio es {average:.2f}')
except:
    print('No se pudo acceder a la información.')