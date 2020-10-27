def celsiusToKelvin(celsius):
    return (celsius + 273.15)

def celsiusToFahrenheit(celsius):
    return (celsius * (9/5) + 32)

try:
    temperature = float(input("Ingresá la temperatura en grados Celsius:"))
    if not temperature == 0:
        print(f'En la escala de Kelvin, los grados que ingresaste son {celsiusToKelvin(temperature)}')
        print(f'En la escala de Fahrenheit, los grados que ingresaste son {celsiusToFahrenheit(temperature)}')
    else:
        print('En la escala de Kelvin, los grados que ingresaste son 0')
        print('En la escala de Fahrenheit, los grados que ingresaste son 0')
except:
    print("No ingresaste un valor correcto.")
