import collections

file = open("noticia.txt", encoding='utf8')
contenido = file.readlines()
palabras = []
no_deseado = ['\ufeff', '—', '\n', '’s', ',', '.']

for line in contenido:    
    for caracter in no_deseado:
      line = line.replace(caracter,'')
    palabras_linea = line.split(' ')
    for palabra in palabras_linea:
      if palabra != '':
        palabras.append(palabra.upper())

frequency = collections.Counter(palabras)
the = frequency['THE']
trump = frequency['TRUMP']
higher_frequency = list(frequency.most_common()[0])
higher_frequency_word = higher_frequency[0]
higher_frequency_count = higher_frequency[1]

print(f'La plabra "The" aparece {the} veces en el texto.')
print(f'La plabra "Trump" aparece {trump} veces en el texto.')
print(f'La palabra con más frecuencia en el texto es {higher_frequency_word} con {higher_frequency_count} apariciones.')
