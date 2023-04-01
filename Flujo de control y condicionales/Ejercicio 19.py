print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

nombre=input("igresar su nombre: ")
edad=int(input("ingresar su edad "))
if edad>=18:
    print(nombre, "es mayor de edad")
elif edad<18:
    print(nombre, "es menor de edad")