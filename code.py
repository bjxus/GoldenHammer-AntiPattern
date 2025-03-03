# Antipatron con listas.

usuarios = [["John", 25], ["Alice", 30], ["Bob", 22], ["Charlie", 28]]

def obtener_edad(nombre, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario[0] == nombre:
            return usuario[1]
    return None  # Si el usuario no existe

# Uso del código
nombre_buscado = "Alice"
edad = obtener_edad(nombre_buscado, usuarios)

if edad:
    print(f"La edad de {nombre_buscado} es {edad} años.")
else:
    print(f"{nombre_buscado} no encontrado.")


