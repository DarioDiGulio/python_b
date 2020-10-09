# Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan - Contraseña: 12345_
# Usuario: Pablo - Contraseña: xDcFvGbHn
# La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.

import json

def checkKeys(user, password):
    users = """{"Juan": {
        "user": "Juan",
        "pass": "12345_"
    },
        "Pablo": {
        "user": "Pablo",
        "pass": "xDcFvGbHn"
    }}"""

    usersData = json.loads(users)
    checked = False
    checked = usersData["Juan"].get("user") == user and usersData["Juan"].get(
        "pass") == password or usersData["Pablo"].get("user") == user and usersData["Pablo"].get("pass")
    return checked


user = input("Ingrese el usuario: ")
password = input("Ingrese la contraseña: ")

if checkKeys(user, password):
    print('Bienvenido!')
else:
    print('Intentá con otras credenciales')
