#programa para sentencia if

#int es para convertir el valor introducido por el usuario en entero
edad = int(input("Ingrese la edad: "))

if edad >= 18:
	print("Eres mayor de edad.")
elif edad == 0:
	print("error de edad ingresada")
else:
	print("eres menor de edad.")