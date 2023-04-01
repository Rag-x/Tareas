print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

num = input("Ingrese un numero: ")

if len(num) != 1:
    print("No se puede procesar el dato.\n!Debe ingresar un solo un numero¡")
elif num in "12345678910":
    print("El numero",num,"Se encuentra en el rango")
else:
    print("No es un numero",num)