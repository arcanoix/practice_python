def suma(valor_uno, valor_dos, valor_tres):
    return valor_uno + valor_dos + valor_tres

def division(valor_uno, valor_dos):
    return valor_uno / valor_dos

def multiplicacion(valor_uno, valor_dos = 10):
    return valor_uno * valor_dos

def multiple_valores():
    return "String", 1, True, 25.6


resultado = suma(10, 25, 30)

division = division(10, 5)

string, entero, bol, floa = multiple_valores()

print(string)
print(entero)
print(bol)
print(floa)

print(division)

print(resultado)
