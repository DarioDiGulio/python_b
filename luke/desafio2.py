##Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, y que muestra en pantalla a qué día de la semana corresponde mediante un número de 0 a 6 (mostrar el número 0 si corresponde a Lunes y 6 si es Domingo)

##Suponemos que el día 0 del año cae un Lunes.

dia = int( input("ingrese numero") )
Lu = 0
Ma = 1
Mi = 2
Ju = 3 
vi = 4
sa = 5
do = 6
y = (dia % 6)
print(y)14
