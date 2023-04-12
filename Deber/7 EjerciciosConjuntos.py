#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE CONJUNTOS
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
numeros = set(range(1, 11))
print(numeros)
#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ellos.
pares = set(range(2, 11, 2))
impares = set(range(1, 11, 2))
print(pares)
print(impares)
print(pares.intersection(impares))
#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas = {"manzana", "banana", "naranja"}
elem = input("Ingresa un elemento: ")
if elem in frutas:
 print("El elemento", elem, "se encuentra en el conjunto.")
else:
 print("El elemento", elem, "no se encuentra en el conjunto.")
#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
conjunto = set(range(1, 6))
conjunto2 = set(range(4, 9))
conjunto .update(conjunto2)
print(conjunto)
#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.
elem = {"leche", "pan", "huevos", "azúcar"}
elem.discard("azúcar")
elem.add("harina")
print(elem)
#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.
nom = {"Juan", "María", "Pedro", "Luisa"}
print(len(nom))
#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.
con = set(range(1, 6))
con2 = set(range(4, 9))
print(con)
print(con2)
print(con.symmetric_difference(con2))
#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.
con = set(range(1, 11))
con2 = set(range(5, 16))
print(con )
print(con2)
print(con .union(con2))
#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.
frutas = {"manzana", "banana", "naranja", "pera"}
print(sorted(frutas))
#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.
con = set(range(1, 11))
con2 = set(range(5, 16))
print(con )
print(con2)
print(con & con2)