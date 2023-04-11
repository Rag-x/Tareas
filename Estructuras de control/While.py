bandera=True
while bandera:
    print("Menu de opciones")
    print("1. Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Divicion")
    print("5.Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion != 5:
        bandera= False
        num1=int(input("Ingrese numero 1: "))
        num2=int(input("Ingrese numero 2: "))
        if opcion == 1:
            print ("La suma es igual a:",num1+num2)
        elif opcion == 2:
            print ("La resta es igual a:",num1-num2)
            break
        elif opcion == 3:
            print ("La multiplicacion es igual a:",num1* num2)
        else:
            print("La Divicion es",num1/num2)
    else:
        bandera = False
        print("Fin de ciclo")
print ("Nueva linea")