print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

dia=int(input("Ingrese un un numero del 1 al 7: "))
if dia==1:
    print("Corresponde al dia Lunes")
elif dia==2:
    print("Corresponde al dia Martes")
elif dia==3:
    print("Corresponde al dia Miercoles")
elif dia==4:
    print("Corresponde al dia Jueves")
elif dia==5:
    print("Corresponde al dia Viernes")
elif dia==6:
    print("Corresponde al dia Sabado")
elif dia==7:
    print("Corresponde al dia Domingo")
else:
    print("El valor ingresado no corresponde a ningun dia de la semana")