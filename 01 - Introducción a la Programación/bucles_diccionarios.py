estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

# Iterar sobre el diccionario utilizando la sintaxis "for clave in diccionario"
# Esto iterará sobre las claves del diccionario
for pais in estudiantes:
    print(pais)
    

# Iterar sobre el diccionario utilizando el método keys() del diccionario
# Esto también iterará sobre las claves del diccionario
for pais in estudiantes.keys():
    print(pais)
    

# Iterar sobre el diccionario utilizando el método values() del diccionario
# Esto iterará sobre los valores del diccionario
for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)
    

# Iterar sobre el diccionario utilizando el método items() del diccionario
# Esto iterará sobre los pares clave-valor del diccionario
for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)
