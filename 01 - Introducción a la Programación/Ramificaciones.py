

def comparar_numeros(primer_numero, segundo_numero):
    """Esta función compara dos números enteros y muestra por pantalla
    si el primer número es mayor, menor o igual al segundo número.
    """
    if primer_numero > segundo_numero:
        print(f'El número {primer_numero} es mayor que el número {segundo_numero}')
    elif primer_numero < segundo_numero:
        print(f'El número {segundo_numero} es mayor que el número {primer_numero}')
    else:
        print("Los dos números ingresados son iguales")

# Pedimos al usuario que ingrese dos números enteros
primer_numero = input("Escribe un número entero: ")
segundo_numero = input("Escribe otro número entero: ")

# Validamos que los números ingresados sean realmente enteros
try:
    primer_numero = int(primer_numero)
    segundo_numero = int(segundo_numero)
except ValueError:
    print("Los números ingresados deben ser enteros.")
else:
    # Si los números son válidos, los comparamos
    comparar_numeros(primer_numero, segundo_numero)

