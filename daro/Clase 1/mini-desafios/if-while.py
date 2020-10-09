# Implementar un programa que muestre la siguiente secuencia: 
# 1, 2, 3, 4, 5, 4, 3, 2, 1, 0 
# Para un desafío mayor:** Utilizar un solo *while*, un solo *if* y un solo *else*

i = 1
j = 4

while j >= 0:
    if i <= 5:
        print(i)
        i += 1
    else:
        print(j)
        j -= 1
