# Variables

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

variable = 2023
print(variable)

#2) Imprimir el tipo de dato de la constante 8.5

constante = 8.5
print(type(constante))

#3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(variable))

#4) Crear una variable que contenga tu nombre

nombre = "Anuar"

#5) Crear una variable que contenga un número complejo

num_complejo = 1 + 2j

#6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(num_complejo))

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

import math

pi = round(math.pi,4)
print(pi)

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

true1 = "True"
true2 = True

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(true1))
print(type(true2))

#10) Asignar a una variable, la suma de un número entero y otro decimal

suma = 2 + 3.5

#11) Realizar una operación de suma de números complejos

"""se crea un  objeto complex"""
z1 = complex(3,4)
z2 = complex(2,5)

z3 = z1 + z2
print(z3)



#12) Realizar una operación de suma de un número real y otro complejo

real_number = 13
complex_number = complex(2,5)

suma = real_number + complex_number
print(suma)

#13) Realizar una operación de multiplicación

multi = 2 * 3

#14) Mostrar el resultado de elevar 2 a la octava potencia

base = 2
potencia = 8
resultado = base ** potencia
print(resultado)

"""opción 2 usando la función pow"""

resultado = pow(2,8)
print(resultado)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

div = 27 / 4
print(f'el cociente es {div}')




#16) De la división anterior solamente mostrar la parte entera

entera = 27 // 4
print(f'la parte entera sería {entera}')


#17) De la división de 27 entre 4 mostrar solamente el resto

resto = 27 % 4
print(f'solo el resto sería {resto}')


#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

obetener_27 = 4 * entera + resto # 4 * (27 // 4) + (27 % 4)

print(f'el resultado sería {obetener_27}')


#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

"""es una concatenación"""

var_1 = "CR7 "
var_2 = "m1s0g1n0"
result = var_1 + var_2
print(f'el resultado es {result}')


#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
a = "2"
b = 2
evaluar = a == b
print(f'el resultado de la evaluación es {evaluar}')
"""Esto ocurre porque son dos tipos de datos diferentes uno es un str y el otro es un entero"""


#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

evaluar = int(a) == b
print(f'el resultado de la evaluación es {evaluar}')


#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

"""el error es porque la "," se usa como separador decimal y debería ser "." por tanto, debe cambiar la  , por un . y así funcionará"""

a = float("3.8")
print(a)



#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

variable = 3
variable -= 1
print(f'el nuevo valor de la variable es {variable}')



#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

resultado = 1 << 2
print(resultado)



#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

num = 2
string_1 = "2"

operacion = int(string_1) + num
print(operacion)

operacion2 = string_1 + str(num)
print(operacion2)



#26) Realizar una operación válida entre valores de tipo entero y string

concatenar = "ha " * 5
print(concatenar)
