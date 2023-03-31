#9. Calificación de un examen. Ingrese la puntuación de un examen.
#Si es >= 90 La calificación es A, si es >= 80 La calificación es B,
#si es >= 70 La calificación es C,
#si >= 60 La calificación es D,
#sino La calificación es F,

print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

num = int (input("Ingrese la puntuacion del examen: "))
if num >= 90 :
    print ("La calificacion es A")
elif num >= 80:
    print ("La calificacion es B")
elif num >=70:
    print ("La calificacion es C")
elif num >= 60:
    print ("La calificacion es D")
else :
    print ("La calificacion es F")