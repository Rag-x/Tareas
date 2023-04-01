#10. Determinar si un año es bisiesto.
#Es divisible entre 4, pero no es divisible entre 100.
#Es divisible entre 400.

#Por ejemplo, los años 2000 y 2020 son bisiestos 
#porque son divisibles entre 400, mientras que el año 1900 no es bisiesto
#porque es divisible entre 100 pero no entre 400.
print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")
año=int (input("Ingrese el año: "))

if año % 4 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0:
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es bisiesto")