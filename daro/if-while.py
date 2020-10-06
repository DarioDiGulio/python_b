# Implementar un programa que muestre la siguiente secuencia: 
# 1, 2, 3, 4, 5, 4, 3, 2, 1, 0 
# Para un desafío mayor:** Utilizar un solo *while*, un solo *if* y un solo *else*

index = 1

while index >= 1:
    print(index)
    if index < 5:
        index = index + 1
    else: 
        index = index - 1
