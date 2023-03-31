# 5.Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")
salario =float (input("Ingrese el sueldo"))
inpuesto = 0
if salario < 10000:
    print("El impuesto es de 5%")
    inpuesto=0,5
elif salario >= 10000 and salario <= 20000:
    print ("El impuesto es del 15%")
    inpuesto=0,15
elif salario >=20000 and salario <=35000:
    print ("El impuesto es del 20%")
    inpuesto=0,20
elif salario >=35000 and salario <=60000:
    print ("El impuesto es del 30 %")
    inpuesto=0,30
elif salario >=60000:
    print ("El impuesto es del 45%")
    inpuesto =0,45
    total=salario * inpuesto 
    print("El total es igual a: ",total) 