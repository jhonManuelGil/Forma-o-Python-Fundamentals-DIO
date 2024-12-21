""" 
é uma estrutura de dados muito versátil e poderosa que permite armazenar coleções de elementos,
onde cada elemento é composto por um par de valores-chave. Ao contrário das listas ou tuplas, que são
indexados por números inteiros, os dicionários são indexados por chaves, que podem ser de diferentes
tipos imutáveis ​​(como strings, números ou tuplas).

"""
# 1. Operaciones básicas con diccionarios
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a valores por clave
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

# Modificar la edad
persona["edad"] = 31
print("\nEdad después de modificar:", persona["edad"])

# Añadir nueva clave 'profesión'
persona["profesion"] = "Ingeniero"
print("\nDiccionario después de añadir profesión:", persona)

# Eliminar la clave 'ciudad'
del persona["ciudad"]
print("\nDiccionario después de eliminar 'ciudad':", persona)

# Verificar si la clave 'edad' existe
if "edad" in persona:
    print("\nLa clave 'edad' existe en el diccionario.")
else:
    print("\nLa clave 'edad' no existe en el diccionario.")


# 2. Operaciones con diccionarios de listas
productos = {
    "manzana": 1.2,
    "plátano": 0.5,
    "naranja": 0.8
}

# Mostrar todos los productos y sus precios
print("\nProductos y precios:")
for producto, precio in productos.items():
    print(f"{producto}: {precio}€")

# Añadir un nuevo producto
productos["uva"] = 2.0
print("\nDespués de añadir 'uva':", productos)

# Modificar el precio de un producto
productos["plátano"] = 0.6
print("\nDespués de modificar el precio de 'plátano':", productos)

# Eliminar un producto
del productos["naranja"]
print("\nDespués de eliminar 'naranja':", productos)


# 3. Diccionarios anidados
escuela = {
    "nombre": "Carlos",
    "edad": 16,
    "asignaturas": ["Matemáticas", "Lengua", "Ciencias"]
}

# Mostrar la información del estudiante
print("\nInformación del estudiante:")
print("Nombre:", escuela["nombre"])
print("Edad:", escuela["edad"])
print("Asignaturas:", escuela["asignaturas"])

# Añadir una nueva asignatura
escuela["asignaturas"].append("Historia")
print("\nDespués de añadir 'Historia' a las asignaturas:", escuela["asignaturas"])

# Modificar la edad del estudiante
escuela["edad"] = 17
print("\nEdad después de modificar:", escuela["edad"])

# Eliminar una asignatura
escuela["asignaturas"].remove("Ciencias")
print("\nDespués de eliminar 'Ciencias' de las asignaturas:", escuela["asignaturas"])
