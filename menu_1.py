#programa menu con opcion de seleccion
print("Bienvenido al sistema, elige que opcion opinas de python ")
opcion = "z"
	
while opcion < "a" or opcion > "c":
	print ("a) adoro python")
	print ("b) detesto python")
	print ("c) no se que es python")

	opcion = input("opcion: ")

	if opcion == "a":
		print("me alegra que te guste")
	elif opcion == "b":
		print ("que mal")
	elif opcion == "c":
		print ("ya deberias aprenderlo")
	else:
		print("Tu opcion no es valida")