"""
Un programa que de a elegir y que calculo hasta n

Un programa que calcule hasta que el termino sea >= n dado

[Iterativa y Recursiva] Choose one

0 1 -> SIEMPRE. 0 no es, 1 es 1

Parar en un termino o en una cantidad (>=")
"""

# Fn = Fn-1 + Fn-2  RECURSIVA


def fibonacci(aux1, aux2, numero_veces=None, cantidad_aproximada=None):
    # numero_veces = 10
    iteracion = 0
    if numero_veces is not None:
        n = numero_veces
    else:
        n = 999
    # n = numero_veces if numero_veces is not None else n = 9999
    while iteracion < n:
        # print(f"Aux2 = {aux2} + {aux1}")

        aux1 = aux1 + aux2

        # print(f"Aux 2: {aux2}")
        # print(f"Aux1 = {aux2} - {aux1}")
        # print(f"Aux 1: {aux1}")

        aux2 = aux1 - aux2

        # print(f"Aux1: {aux1} || Aux2: {aux2}")
        # print(f"Aux 2: {aux2}")
        # aux1, aux2 = aux2, aux1 + aux2
        # aux1 = aux2
        # aux2 = aux1 + aux2

        if cantidad_aproximada is not None and aux1 >= cantidad_aproximada:
            print(f"{aux1} Se apoxima a {cantidad_aproximada}")
            break
        iteracion += 1
    return aux1


def input_usuario():
    while True:
        try:
            opcion = int(input())
            break
        except ValueError as error:
            print("Ha ocurrido un error.", error)
        finally:
            return opcion


def decision(input):
    if input == 0:
        print("Ingresa el numero de terminos")
        numero_terminos = input_usuario()
        return 0, numero_terminos
    elif input == 1:
        print("Ingresa la cantidad aproximada: ")
        cantidad_maxima = input_usuario()
        return 1, cantidad_maxima


def main():
    print("""
0 Para ingresar el numero de terminos
1 Para ingresar una cantidad aproximada
""")
    opcion = input_usuario()
    aux, numero = decision(opcion)
    if aux == 0:
        resultado = fibonacci(0, 1, numero_veces=numero)
    elif aux == 1:
        resultado = fibonacci(0, 1, cantidad_aproximada=numero)

    print(resultado)


main()
