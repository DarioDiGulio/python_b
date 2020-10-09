# Mostrar la siguiente secuencia de datos utilizando la instrucción for y la instrucción if: 
# 0, 1, 4, 9, 16, 25, 6, 7, 8, 9

i = 0
j = 6

for j in range(0, 10):
    if i <= 5:
        print(i * i)
        i += 1
    else:
        print(j)
        j += 1
