import pandas as pan

def print_average(student):
    name = student['Nombre']
    average = (student['Quimica'] + student['Matematica'] + student['Fisica']) / 3
    print(f'El promedio de {name} es {average:.2f}')

try:
    data = pan.read_excel("Datos.xlsx", )
    data_dict = data.to_dict("records")
    for student in data_dict:
        print_average(student)
except:
    print('No se pudo acceder a la información.')
