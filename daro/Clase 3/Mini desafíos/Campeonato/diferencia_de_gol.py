import pandas as pan

try:
    data = pan.read_excel("Tabla1.xlsx", )

    data_dict = data.to_dict("records")

    for equipo in data_dict:
        diferencia_de_gol = equipo['Goles a favor'] - equipo['Goles en contra']
        equipo = equipo['Equipo']
        print(f'Para el equipo {equipo} la diferencia de gol es de {diferencia_de_gol}')
except:
    print('No se pudo acceder a la información.')