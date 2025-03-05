def contar_palabras(texto):
    return len(texto.split())

texto = "Hola, este es un ejemplo del antipatrón Golden Hammer."
print(contar_palabras(texto))  # Salida: 9
