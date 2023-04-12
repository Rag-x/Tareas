###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1. Suma de elementos de una lista: Dada una lista de números, escribe un programa que calcule la suma de todos los elementos de la lista usando un bucle for.
def sum(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
def main():
    opcion = 0
    lista = []
    while opcion != 2:
        print("MENU")
        print("1. Agregar elementos a la lista")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            elemento = int(input("Ingrese un elemento: "))
            lista.append(elemento)
    print("La suma de los elementos de la lista es:", sum(lista))
    print("La lista ingresada es: ", lista)
str(main())
#2. Contar elementos en una lista: Dada una lista de elementos, escribe un programa que cuente cuántos elementos hay en la lista usando un bucle for.
def contar(lista):
    contador = 0
    for elemento in lista:
        contador += 1
    return contador
def main():
    opcion = 0
    lista = []
    while opcion != 2:
        print("MENU")
        print("1. Agregar elementos a la lista")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            elemento = input("Ingrese un elemento: ")
            lista.append(elemento)
    print("La lista ingresada es: ", lista)
    print("La cantidad de elementos en la lista es:", contar(lista))
main()
#3. Imprimir elementos de una lista: Dada una lista de elementos, escribe un programa que imprima cada elemento de la lista en una línea separada usando un bucle for.
def imp(lista):
    for elemento in lista:
        print(elemento)
def main():
    opcion = 0
    lista = []
    while opcion != 2:
        print("MENU")
        print("1. Agregar elementos a la lista")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            elemento = input("Ingrese un elemento: ")
            lista.append(elemento)
    print("La lista ingresada es: ", lista)
    print("Los elementos de la lista son:",)
    imp(lista)
main()
#4. Contar caracteres en una cadena: Dada una cadena de caracteres, escribe un programa que cuente cuántos caracteres hay en la cadena usando un bucle for.
def contar(cadena):
    contador = 0
    for caracter in cadena:
        contador += 1
    return contador

def main():
    opcion = 0
    while opcion != 2:
        print("MENU")
        print("1. Ingresar una cadena")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            cadena = input("Ingrese una cadena: ")
            print("La cadena ingresada es:", cadena)
            print("La cantidad de caracteres en la cadena es:", contar(cadena))
main()
#5. Imprimir caracteres de una cadena: Dada una cadena de caracteres, escribe un programa que imprima cada carácter de la cadena en una línea separada usando un bucle for.
def imprimir(cadena):
    for caracter in cadena:
        print(caracter)

def main():
    opcion = 0
    while opcion != 2:
        print("MENU")
        print("1. Ingresar una cadena")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            cadena = input("Ingrese una cadena: ")
            print("La cadena ingresada es:", cadena)
            print("Los caracteres de la cadena son:")
            imprimir(cadena)
main()
#6. Imprimir los primeros N números naturales: Dado un número entero N, escribe un programa que imprima los primeros N números naturales usando un bucle for.
def imp(n):
    for e in range(1, n+1):
        print(e)

def main():
    opcion = 0
    while opcion != 2:
        print("MENU")
        print("1. Imprimir los primeros N números naturales")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            n = int(input("Ingrese el valor de N: "))
            print("Los primeros", n, "números naturales son:")
            imp(n)
main()
#7. Imprimir los primeros N números pares: Dado un número entero N, escribe un programa que imprima los primeros N números pares usando un bucle for.
def pares(n):
    for i in range(2, 2*n+1, 2):
        print(i)

def main():
    opcion = 0
    while opcion != 2:
        print("MENU")
        print("1. Imprimir los primeros N números pares")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            n = int(input("Ingrese el valor de N: "))
            print("Los primeros", n, "números pares son:")
            pares(n)
main()
#8. Imprimir los primeros N números impares: Dado un número entero N, escribe un programa que imprima los primeros N números impares usando un bucle for.
def impares(n):
    for i in range(1, 2*n, 2):
        print(i)
def main():
    opcion = 0
    while opcion != 2:
        print("MENU")
        print("1. Imprimir los primeros N números impares")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            n = int(input("Ingrese el valor de N: "))
            print("Los primeros", n, "números impares son:")
            impares(n)
main()
#9. Imprimir la tabla de multiplicar de un número: Dado un número entero N, escribe un programa que imprima la tabla de multiplicar de N usando un bucle for.
def multiplicar(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

def main():
    opcion = 0
    while opcion != 2:
        print("MENU")
        print("1. Imprimir la tabla de multiplicar de un número")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            n = int(input("Ingrese el valor de N: "))
            print("La tabla de multiplicar de", n, "es:")
            multiplicar(n)
main()
#10. Imprimir los primeros N números de la serie de Fibonacci: Dado un número entero N, escribe un programa que imprima los primeros N números de la serie de Fibonacci usando un bucle for.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

def main():
    opcion = 0
    while opcion != 2:
        print("MENU")
        print("1. Imprimir los primeros N números de la serie de Fibonacci")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            n = int(input("Ingrese el valor de N: "))
            print("Los primeros", n, "números de la serie de Fibonacci son:")
            fibonacci(n)

main()