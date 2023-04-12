###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contadorAsendente(num):
    cadena=""
    cont = 0    
    while cont <= num:
        cadena+=str(cont)
        cont+=1
    return cadena 
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def contadorDescendente(num):
    cadena = "" 
    while num>= 0:
        cadena += str(num)
        num -= 1
    return cadena 
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def sumaNumeros(num):
    suma = 0
    e = 0
    while e <= num:
        suma += e
        e += 1
    return suma
#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.
def multiplos(num):
    p = 1
    contador = 0
    cadena = ""
    while contador < 10:
        cadena += str(num * p) + " "
        p += 1
        contador += 1
    return cadena
#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
import random
def adivi(aleatorio):
    numero=0
    while numero != aleatorio:
        numero=int(input("Ingrese el numero del 1 al 100:"))
        if numero> aleatorio:
            print("El numero ingresado es mayor al numero a adivinar")
        elif numero < aleatorio:
            print("El numero ingresado es menor al numero a adivinar")
        else:
            print("Felicidades adivinaste el numero",numero)
            
aleatorio= random.randint(1,100)
#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def contador1(cadena):
    vocales = 'aeiou'
    contador = 0
    i = 0
    while i < len(cadena):
        if cadena[i] in vocales:
            contador += 1
            i += 1
    return contador
#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suman(numero):
    sumap = 0
    i = 0
    while i <= numero:
        if i % 2 == 0:
            sumap += i
        i += 1
    return sumap
#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def calcularp(base, exponente):
    resultado = 1
    i = 0

    while i < exponente:
        resultado *= base
        i += 1
    return resultado
#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def calcularp(lista):
    suma = 0
    contador = 0
    i = 0
    while i < len(lista):
        suma += lista[i]
        contador += 1
        i += 1
    promedio = suma / contador
    return promedio
#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def contarp(cadena):
    contador = 0
    palabraa = ""
    i = 0
    while i < len(cadena):
        if cadena[i] != " ":
            palabraa += cadena[i]
        else:
            if palabraa != "":
                contador += 1
                palabraa = ""
        i += 1
    if palabraa != "":
        contador += 1
    return contador
##############MENU DE OPCIONES###################
opcion =1
while opcion>=0 and opcion<=10:
    print("############# Menu de Opciones ##############")
    print("1.contador Ascendente")
    print("2.contador Decendente")
    print("3.suma de Numeros")
    print("4.Factorial")
    print("5.Adivinar un Numero")
    print("6.Contador de vocales")
    print("7.Suma de numeros pares")
    print("8.Calculo de potencia")
    print("9.Clculo de promedio")
    print("10.Contador de palabras")
    print("0.Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion ==0:
        print("Se a seleccionado la opcion salir")
        break
    elif opcion ==1:
        print ("A seleccionado la opcion de contador acendente")
        num=int(input("Ingrse un numero: "))
        print(contadorAsendente(num))
    elif opcion ==2:
        print ("A seleccionado la opcion de contador decendente")
        num=int(input("Ingrse un numero: "))
        print(contadorDescendente(num))
    elif opcion ==3:
        print ("A seleccionado la opcion de suma de numeros")
        num=int(input("Ingrse un numero: "))
        print(sumaNumeros(num))
    elif opcion ==4:
        print ("A seleccionado la opcion de Factorial")
        num=int(input("Ingrse un numero: "))
        print(multiplos(num))
    elif opcion ==5:
        print ("A seleccionado la opcion de adivinar un numero")
        print (str (aleatorio))
        adivi(aleatorio)
    elif opcion ==6:
        print ("A seleccionado la opcion de contador de vocales")
        cadena=str(input("Ingrse las vocales: "))
        print(contador1(cadena))
    elif opcion ==7:
        print ("A seleccionado la opcion de suma de numeros pares")
        numero = int(input("Ingrese un número entero positivo: "))
        resultado = suman(numero)
        print("La suma de todos los números pares desde 0 hasta {} es: {}".format(numero, resultado))
    elif opcion ==8:
        print ("A seleccionado la opcion de calculo de potencia")
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        potencia = calcularp(base, exponente)
        print("El resultado de {} elevado a {} es: {}".format(base, exponente, potencia))
    elif opcion ==9:
        print ("A seleccionado la opcion de calculo de promedio")
        numeros = input("Ingrese una lista de números separados por comas: ")
        numerosl = [int(numero) for numero in numeros.split(',')]
        promedio = calcularp(numerosl)
        print("El promedio de los números es:", promedio)
    elif opcion ==10:
        print ("A seleccionado la opcion de contador de palabras")
        cadena = input("Ingrese una cadena de texto: ")
        cantidadp = contarp(cadena)
        print("La cantidad de palabras en la cadena es:", cantidadp)