# Cálcular la nota de un alumno es una tarea cotidiana de un profesor. 
# Esta tarea suele realizarse a mano o en excel muchas veces. En esta ocasión la haremos en python.
# Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.
# Reescribir la función anterior modificandola para asignar una importancia al primer examen de 20%, 
# al segundo de 50% y al tercero de 30%.
# Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción if, 
# si el alumno aprobó en cada caso (suponga que 4 es la nota de aprobación).
import random

def obtener_promedio(nota1, nota2, nota3):
    return round(((nota1 + nota2 + nota3) / 3),2)

def obtener_promedio_ponderado(nota1, nota2, nota3):
    nota1_ponderada = nota1 * .2
    nota2_ponderada = nota2 * .5
    nota3_ponderada = nota3 * .3
    return (obtener_promedio(nota1_ponderada, nota2_ponderada, nota3_ponderada))

def nota():
    return random.randint(1,10)

def aprobo(promedio):
    if promedio >= 4:
        print(f'Con un promedio de {promedio} aprobó.')
    else:
        print(f'Con un promedio de {promedio} no aprobó.')

for i in range(3):
    print('Promedio sin ponderación')
    avg = obtener_promedio(nota(), nota(), nota())
    aprobo(avg)
    print('Promedio con ponderación')
    avg_pond = obtener_promedio_ponderado(nota(), nota(), nota())
    aprobo(avg_pond)


