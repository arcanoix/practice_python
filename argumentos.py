# * siginifica que puede aguantar multiple elementos
def suma(*args):
    resultado = 0
    for valor in args:
        resultado = resultado + valor
    return resultado

resultado = suma(10, 6 ,9 ,9)
print(resultado)
