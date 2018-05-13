# Calculadora version de python es 3
print("****************************************")
print("****************************************")
print("***** Bienvenido a la calculadora ******")
print("****************************************")
print("****************************************")

# ingresar numeros
numero_uno = input("Ingrese numero uno: ")
numero_dos = input("Ingrese numero dos: ")

#listar tipo de operacion
print("****************************************")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divicion")

seleccion = int(input("Digite la operacion a realizar: "))

if(seleccion == 1):
	#resultado de la suma
	suma = int(numero_uno) + int(numero_dos)	
	#imprimri pantalla 
	print("La suma de dos numeros es : " + str(suma))
elif(seleccion == 2):
	resta = int(numero_uno) - int(numero_dos)	
	#imprimri pantalla 
	print("La resta de dos numeros es : " + str(resta))
elif(seleccion == 3):
	multiplicacion = int(numero_uno) * int(numero_dos)	
	#imprimri pantalla 
	print("La multiplicacion de dos numeros es : " + str(multiplicacion))
elif(seleccion == 4):
	division = int(numero_uno) / int(numero_dos)	
	#imprimri pantalla 
	print("La division de dos numeros es : " + str(division))
else:
	print('Opcion incorrecta')