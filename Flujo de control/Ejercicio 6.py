# 6. Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#En caso de introducir una opción inválida, el programa informará de que no es correcta.

print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce un número: ") )
num = 0
           
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
num = int(input("Introduce un número: ") )     

if num == 1:
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif num == 2:
    print("La resta de",n1,"-",n2,"es",n1-n2)
elif num == 3:
    print("La multiplicacion de",n1,"*",n2,"es",n1*n2)
else:
    print("Opción incorrecta")