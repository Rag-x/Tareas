#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#Crear un diccionario vacío:
dic={}
#Agregar elementos a un diccionario:
dic["jb"] = "Juan B"
dic["bj"] = "Barbecho J"
dic["ck"] = "Carlos K"
#Acceder a un valor en un diccionario:
valor=(dic["jb"])
print(valor)
#Verificar si una llave existe en un diccionario:
if "jb" in dic:
    print("La clave 'bj' existe en el diccionario")
#Eliminar un elemento de un diccionario:
del dic["jb"]
print("Elemento eliminado",dic)
#Imprimir las llaves de un diccionario:
for e in dic.keys():
    print(e)
#Imprimir los valores de un diccionario:
for e in dic.values():
    print(e)
#Imprimir las llaves y valores de un diccionario:
for e in dic.items():
 print("la llave y el valor es:",e) 


