# Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, 
# y que muestra en pantalla a qué día de la semana corresponde mediante un número de 0 a 6 
# (mostrar el número 0 si corresponde a Lunes y 6 si es Domingo)
# Suponemos que el día 0 del año cae un Lunes.

def get_dia_elegido(num):
    resto = num % 7
    dia = ''

    if resto == 0:
        dia = 'Lunes'
    elif resto == 1:
        dia = 'Martes'
    elif resto == 2:
        dia = 'Miércoles'
    elif resto == 3:
        dia = 'Jueves'
    elif resto == 4:
        dia = 'Viernes'
    elif resto == 5:
        dia = 'Sábado'
    elif resto == 6:
        dia = 'Domingo'
    
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
