# Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, 
# y se muestre a la salida el promedio de los tres números.

num1 = input("Ingresá un número: ")
num2 = input("Ingresá otro número: ")
num3 = input("Ingresá el último número: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    promedio = (num1 + num2 + num3) // 3
    print(f'El promedio es {promedio}')
except:
    print("No ingresaste números válidos.")
