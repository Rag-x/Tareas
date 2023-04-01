#20. Escribir un programa 
#que pregunte al usuario una cantidad de días y muestre por pantalla 
#cuantas horas, minutos y segundos hay en dicha cantidad de días.

print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

d = int(input("Introduce una cantidad de días: "))

horas = d * 24
minutos = horas * 60
segundos = minutos * 60

print("En", d, "días hay:")
print(horas, "horas.")
print(minutos, "minutos.")
print(segundos, "segundos.")