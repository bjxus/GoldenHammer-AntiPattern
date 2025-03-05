def contar_palabras(texto):
    contador = 0
    palabras = texto.split()  # Separa las palabras usando espacios como delimitador
    for palabra in palabras:
        contador += 1  # Incrementa el contador por cada palabra encontrada
    return contador

texto = "Hola, este es un ejemplo del antipatrón Golden Hammer."
print(contar_palabras(texto))  # Salida: 9

