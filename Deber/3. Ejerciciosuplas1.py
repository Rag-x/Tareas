#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla vacía:
tupla=()
#Crear una tupla con algunos elementos:
tupla=("hola",12,1,2,"cuatro")
#Acceder a un elemento de la tupla:
print (tupla[4])
#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):
tupla[2] = 5
#Concatenar dos tuplas:
tupla1=(1,2,3,4)
tupla2=(5,6,7,8)
tu=tupla1+tupla2
print (tu)
#Obtener la longitud de una tupla:
print (len(tupla))
#Convertir una tupla en una lista:
m=list(tupla)
print(m)
#Convertir una lista en una tupla:
tupla=tuple(m)
print(tupla)




