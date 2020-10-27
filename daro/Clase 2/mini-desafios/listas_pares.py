# Crear una lista con los números pares menores a 50.

def es_par(number):
    return number % 2 == 0

numbers = []

for i in range(0, 50):
    if es_par(i):
        numbers.append(i)

print(numbers)