# Definimos la función "coordenadas" que devuelve una tupla con dos elementos: 5 y 4
def coordenadas():
    return(5,4)

# Llamamos a la función "coordenadas" y asignamos el resultado a la variable "resultado"
resultado = coordenadas()

# Imprimimos el valor de "resultado"
print(resultado)  # (5, 4)

# Desempaquetamos la tupla en dos variables "x" e "y"
x, y = coordenadas()

# Imprimimos el resultado de multiplicar "x" por 2
print(x * 2)  # Imprime 10

# Imprimimos el resultado de multiplicar "y" por -3
print(y * -3)  # Imprime -12
