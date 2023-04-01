#18. Escribir un programa que pida al usuario una frase y determine si 
#es un palíndromo. Ignorar espacios en blanco y mayúsculas/minúsculas al 
#determinar si la frase es un palíndromo o no.
print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

fra = input("Introduce una frase: ")
fra = fra.lower().replace(" ", "")

if fra == fra[::-1]:
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")