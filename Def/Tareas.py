bandera=True
def suma (num1,num2):
    return num1+num2
def res (num1,num2):
    return num1-num2
def mul (num1,num2):
    return num1*num2
def div (num1,num2):
    return num1/num2
def saludo():
    print("Hola Juan")
def formateo(nombre,apellido):
    print(nombre,apellido)
while bandera:
    print("Menu de opciones")
    print("1. Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Divicion")
    print ("5.Saludo")
    print("6.Formateo")
    print("7.Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion != 7:
        bandera= False
        num1=int(input("Ingrese numero 1: "))
        num2=int(input("Ingrese numero 2: "))
        if opcion == 1:
            print ("La suma es igual a:",suma(num1,num2))
        elif opcion == 2:
            print ("La resta es igual a:",res(num1,num2))
        elif opcion == 3:
            print ("La multiplicacion es igual a:",mul(num1,num2))
        elif opcion == 4:
            print("La Divicion es",div(num1,num2))
        elif opcion == 5:
            saludo()
        else:  
            formateo("Juan","Bravo")     
    else:
        bandera = False
        print("Fin de ciclo")
       
print ("Nueva linea")
