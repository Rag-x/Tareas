# 6. Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#En caso de introducir una opción inválida, el programa informará de que no es correcta.

print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

val = float(input("Ingrese un valor numerico: ") )
val2 = float(input("Introduce otro valor numerico: ") )
num = 0
           
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
num = int(input("Introduce un número: ""\n") )     

if num == 1:
    print("La suma de",val,"+",val2,"es",val+val2)
elif num == 2:
    print("La resta de",val,"-",val2,"es",val-val2)
elif num == 3:
    print("La multiplicacion de",val,"*",val2,"es: " ,val*val2)
else:
    print("Opción incorrecta")