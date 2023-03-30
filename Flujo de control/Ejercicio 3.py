# 3.Escribir un programa que almacene la cadena de caracteres <b>contraseña</b> en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide 
# con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")
contra="Juan123"
x= input ("ingrese su contraseña: ")
if x.lower() == contra:
    print ("Contraseña correcta")
else:
    print ("Contraseña incorecta")