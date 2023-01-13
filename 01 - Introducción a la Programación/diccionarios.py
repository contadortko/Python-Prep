"""Los diccionarios son muy útiles para almacenar datos relacionados y son muy comunes en Python.
para crear un diccionario se utilizan las llaves {} y su sintaxis es la siguiente:

diccionario = {clave: valor, clave: valor, ...}"""

my_dict = {
    "Nombre": "Anuar",
    "Apellido": "Monterrosa",
    "Edad": 35
}
print(my_dict)

"""Para acceder a un dato de un diccionario se llama al diccionario y la llave"""

print(my_dict["Nombre"])

"""Para acceder a una llave pero esta no existe,
podemos definir un valor determinado"""

print(my_dict.get("email","llave no existe"))

"""para acceder a una llave que si exista"""

print(my_dict.get("Edad","llave no existe"))

print("""Para modificar un valor referenciamos su llave""")

my_dict["Edad"]= "edad modificada"
print(my_dict)

print("""para eliminar un elemento usamos el método -del- y referenciamos su llave""")

del my_dict["Edad"]
print(my_dict)

print("para obtener las llaves del diccionario se usa un método -for loop-")

for i in my_dict.keys():
    print(i)

print("para obtener los valores de las llaves se usa un método -for loop-")

for i in my_dict.values():
    print(i)

print("Para consultar llaves y valores usarmos items")

for i in my_dict.items():
    print(i)

print("Para revisar si una llave existe en el diccionario usamos -in_")

print("edad" in my_dict)
print("Nombre" in my_dict)