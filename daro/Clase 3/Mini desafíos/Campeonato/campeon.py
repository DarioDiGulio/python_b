import pandas as pan
import numpy as np

try:
    data = pan.read_excel("Tabla1.xlsx", )
    score = np.array(data.to_dict('list')['Puntos'])
    teams = np.array(data.to_dict('list')['Equipo'])
    max_score = np.amax(score)
    position_max_score = np.where(score == max_score)[0][0]
    print(f'El ganador es {teams[position_max_score]}')
except:
    print('No se pudo acceder a la información.')
