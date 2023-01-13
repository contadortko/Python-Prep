# Pedimos al usuario que ingrese el número de veces que quiere que se repita el bucle
veces = input("¿Cuántas veces quieres que se repita el bucle? ")

# Validamos que el número ingresado sea un entero
try:
    veces = int(veces)
except ValueError:
    print("El número ingresado debe ser un entero.")
else:
    # Inicializamos el contador
    numero_actual = 1

    # Repetimos el bucle hasta que se alcance el límite
    while numero_actual <= veces:
        print(numero_actual)
        numero_actual += 1
        if numero_actual >20: #con esto el bucle se rompe si se ingresa un numero mayor a 20.
            break
    

