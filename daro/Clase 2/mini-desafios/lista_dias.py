# Crear una lista con el nombre de los días de la semana. 
# Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, 
# que determine a qué día de la semana corresponde mediante un número de 0 (Lunes) a 6 (Domingo) 
# y luego muestre en pantalla el elemento correspondiente de la lista, o sea, el día de 
# la semana en forma de texto (suponemos que el día 0 del año es Lunes).

days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def get_dia_elegido(num):
    resto = num % 7
    dia = ''

    if resto == 0:
        dia = days[0]
    elif resto == 1:
        dia = days[1]
    elif resto == 2:
        dia = days[2]
    elif resto == 3:
        dia = days[3]
    elif resto == 4:
        dia = days[4]
    elif resto == 5:
        dia = days[5]
    elif resto == 6:
        dia = days[6]
    
    return dia

ERROR_MESSAGE = "No ingresaste un número válido."
MIN, MAX = 0, 364
num = input(f'Ingresá un número entre {MIN} y {MAX}: ')

try:
    num = int(num)
    if num >= MIN and num <= MAX:
        dia_elegido = get_dia_elegido(num)
        print(f'El número ingresado corresponde a un {dia_elegido}')
    else:
        print(ERROR_MESSAGE)
except:
    print(ERROR_MESSAGE)