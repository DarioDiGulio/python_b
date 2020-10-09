# La conjetura del Dr. Lothar
# Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:
# Si el numero es par, se debe dividir por  2 .
# Si el numero es impar, se debe multiplicar por  3  y sumar  1 .
# Este proceso se repite hasta llegar al numero  1  y luego muestra en pantalla la cantidad de pasos que tardó en llegar.
# Ejemplo para  n=6 :
# 6,3,10,5,16,8,4,2,1 
# Resultado = 8


def es_par(num):
    return num % 2 == 0

try:
    user_num = int(input("Ingresá un número entero por favor: "))
    index = 0

    while user_num != 1:
        if es_par(user_num):
            user_num = user_num // 2
        else:
            user_num = (user_num * 3) + 1
        print(user_num)
        index += 1
    
    print(f'Se tardó {index} veces en llegar a {user_num}')
except:
    print("El valor ingresado no es correcto.")
