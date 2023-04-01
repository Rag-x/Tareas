#9. Calificación de un examen. Ingrese la puntuación de un examen.

print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")
print ("Detalles:\nCalificacion de un examen")

num = float(input("Ingrese la puntuacion del examen: "))
if  (num >= 9.5) and (num <= 10) :
    print ("El estudiante tiene un rendimiento exelente")
elif (num >= 8.5) and  (num < 9.5):
    print ("El estudiante es muy bueno")
elif  (num >=7.00) and  (num < 8.5):
    print ("El estudiante es bueno")
elif  (num >= 4.00) and  (num < 7.00):
    print ("El estudiante es regular")
elif  (num >=  0.00) and  (num < 4.00) :
     print ("El estudiante es deficiente")
    