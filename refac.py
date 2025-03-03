# Manera correcta o mas eficiente utiilizando diccionarios.

usuarios = {
    "John": 25,
    "Alice": 30,
    "Bob": 22,
    "Charlie": 28
}

def obtener_edad(nombre, diccionario_usuarios):
    return diccionario_usuarios.get(nombre, None)  # Búsqueda en O(1)

nombre_buscado = "Alice"
edad = obtener_edad(nombre_buscado, usuarios)

if edad:
    print(f"La edad de {nombre_buscado} es {edad} años.")
else:
    print(f"{nombre_buscado} no encontrado.")

