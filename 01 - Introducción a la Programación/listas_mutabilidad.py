"""Las listas son secuencias de objetos, pero a diferencia de las tuplas y rangos, sí son mutables.
Es posible iterar con ellas, y cuando modificas una lista, pueden existir efectos secundarios (side effects).
las listas se crean utilizando corchetes []"""

"""Aquí hay algunos de los métodos más comunes que se pueden utilizar con las listas en Python:

append(elemento): añade un elemento al final de la lista.
extend(lista): añade todos los elementos de otra lista al final de la lista actual.
insert(índice, elemento): inserta un elemento en la posición especificada por el índice.
remove(elemento): elimina el primer elemento de la lista que tenga el valor especificado.
pop(índice): elimina el elemento en la posición especificada por el índice y devuelve su valor. Si no se proporciona un índice, se elimina el último elemento de la lista.
clear(): elimina todos los elementos de la lista.
index(elemento): devuelve el índice de la primera ocurrencia del elemento especificado en la lista.
count(elemento): devuelve el número de veces que aparece el elemento especificado en la lista.
sort(): ordena los elementos de la lista de menor a mayor.
reverse(): invierte el orden de los elementos de la lista."""

my_list = [1,2,3,4,5,6,7,8,9]

#accedemos al primer indice
print(my_list[0]) #imprime el elemento 1
print(my_list[1:]) # imprime el elemento 2 hacía delante es decir del 2 al 9
print(my_list[0:5]) #imprime el elemento 1 al 5

#agregamos un nuevo elemento a la lista existente
my_list.append(0)
print(my_list) #verificamos el nuevo elemento agregado

 #modificamos un elemento de la lista
my_list[5] = "Anuar" #cambia el elemento 6 por el str "Anuar"
print(my_list)

#Eliminamos el ultimo elemento de la lista

my_list.pop()
print(my_list)

#eliminamos el 4to elemento de la lista
my_list.pop(4)
print(my_list)

#clonar una lista es mejor que mutarla así si modificamos una lista su contraparte clonada no se verá afectada
#creamos la lista a
a =[1,2,3]
#con la variable b clonaremos la lista a
b = list(a)
#si removemos el ultimo elemento de la lista a no se verá reflejado en b
a.pop()

print(a)
print(b)

#agregamos una lista dentro de otra lista
a.extend(b)
a.sort()
print(a)