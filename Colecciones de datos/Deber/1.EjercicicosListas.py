###CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 5
num = [1, 2, 3, 4, 5]

#2. Accede al elemto 3 de la lista:
ele = num[2]
print("Elemento 3:", ele)

#3. Modificar un elemento de la lista:
num[1] = 6
print("Lista modificada:", num) 

#4. Agregar el elemento 9 al final de la lista:
num.append(9)
print("Lista con elemento 9 agregado:", num) 

#5. Eliminar el elemento 2 de la lista:
num.remove(2)
print("Lista con elemento 2 eliminado:", num) 

#6. Recorrer una lista con un bucle for:
for numero in num:
  print(numero)

#7. Ordenar una lista:
num.sort()
print("Lista ordenada:", num)

#8. Obtener la longitud de una lista:
lon = len(num)
print("Longitud de la lista:", lon) 

#9. Comprobar si un elemento está en la lista:
if 7 in num:
   print("El número 7 está en la lista.")
else:
   print("El número 7 no está en la lista.") 