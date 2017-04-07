#Sistema de calculo de area pero con salida de formato
print ("Programa calculo del area de un triangulo")

base = float(input("ingrese el valor de la base: "))
altura = float(input("ingrese el valor de la altura:"))

area = base * altura / 2.0
#se coloca %f porque la variable base es de float y los numeros que tiene
#son cantidad de caracteres y decimales. 
print("La base es %6.2f. y el area es %5.1f" %(base, area))