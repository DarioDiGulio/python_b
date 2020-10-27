# Hacer un programa que permita ingresar un nombre y un apellido usando dos veces la función input( ). 
# Luego debe crear la variable nombre_y_apellido que contenga ambos datos separados por un espacio. 
# Un fabricante de tarjetas admite la impresión de hasta 26 caracteres para el nombre del dueño de la tarjeta, 
# el programa debe imprimir "Nombre admitido" si nombre_y_apellido cumple con esta restricción y "Nombre no admitido" 
# en caso contrario (el espacio cuenta como uno de los 26 caracteres disponibles).
# Para un desafío mayor: Si nombre_y_apellido cumple la restricción, mostrar el nombre y apellido. 
# En caso contrario nombre_y_apellido debe valer la inicial del nombre y luego el apellido separado por un espacio. 
# Si todavía no se cumple la restricción entonces el valor será la inicial del nombre y las primeras 24 letras del apellido. 
# Mostrar el nombre resultante.

def input_string(concept):
    return input(f'Ingrese {concept}: ')

name = input_string('el nombre')
surname = input_string('el apellido')
full_name = f'{name} {surname}'

if len(full_name) > 26:
    full_name = f'{name[0]} {surname}'
if len(full_name) > 26:
    full_name = f'{name[0]} {surname[:24]}'

print(f'El nombre será admitido como {full_name}')
