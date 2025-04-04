# Fn = Fn-1 + Fn-2
def fibonacci(numero):
    if numero in (0, 1):
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


print(fibonacci(10))
