def esMultiploDeCinco(num):
    return num % 5 == 0

def esMultiploDeTres(num):
    return num % 3 == 0

def esMultiploDeAmbos(num):
    return esMultiploDeCinco(num) and esMultiploDeTres(num)


for i in range(1, 100):
    number = str(i)
    if esMultiploDeAmbos(i):
        number = number + ' N3N5'
    elif esMultiploDeCinco(i):
        number = number + ' N5'
    elif esMultiploDeTres(i):
        number = number + ' N3'
    print(number)