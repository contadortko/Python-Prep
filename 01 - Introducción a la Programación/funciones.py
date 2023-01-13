def aplicar_operaciones(num):
    operaciones = [abs, float,str,int]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    print(resultado)
    return resultado

aplicar_operaciones(int(input("Introduce un número = ")))