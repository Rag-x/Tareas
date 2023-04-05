#tupla= (100,"hola",1,2,3,"Pepe")
#print (tupla[-1])
alumnos= {"nombre":"Juan",
          "apellido":"Perez",
          "cedula":"1105050775",
          "direccion":"Cuenca",
          "email":"juan@gmail.com"}
print (alumnos)
print (alumnos["cedula"])
print (alumnos["email"])
alumnos["cedula"]=1105050775
alumnos["genero"]="Masculino"
print (alumnos,"\n")

instituto={"carreras":["Bigdata","Mecatronica","Saiver seguridad","electricidad","Desarrollo"],
           "materias":["comunicacion","programacion","lenguaje y comunicacion","redes","sistemas"],
           "profesores":["Ochoa","Adriana","Nivicela","Belen","Ana","Veronica"],
          "notas":[70,83,75,76,81,73,72]
           }
print(instituto["carreras"])
print(instituto["materias"])
print(instituto["profesores"])
print(instituto["notas"])
m=round(sum(instituto["notas"])/len(instituto["notas"]))
print ("la suma de la lista es:", m)
promedio=0
for e in (instituto["notas"]):
 promedio+=e
print(promedio/len(instituto["notas"]))
print (round(promedio/len(instituto["notas"])))
print("Valor maximo",max(instituto["notas"]))
nota_minima=min(instituto["notas"])

posicion=((instituto["notas"]).index(nota_minima))

print("La nota minima es:",nota_minima)
print("El nombre de la materia:",instituto["materias"][0])
print("El nombre del profesor:",instituto["profesores"][0])
