"""La comprensión de listas es una técnica de Python que nos permite crear una nueva lista a partir de una expresión iterable.
Es una forma concisa y legible de crear listas a partir de datos existentes."""

my_list = list(range(10)) #crea una lista con números entre 0 y 9
print(my_list)

#creamos una comprensión de lista donde multiplicaremos * 2 cada elemento de la lista

double = [i * 2 for i in my_list]
print(double)

#ahora solo tomaremos los números pares

pares = [i for i in my_list if i % 2 == 0]
print(pares)

#ahora tomaremos los impares
impares = [i for i in my_list if i % 2 != 0]
print(impares)