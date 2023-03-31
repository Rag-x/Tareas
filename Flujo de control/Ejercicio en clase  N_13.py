#Ejercicio 13
#Crear un programa para determinar si un número es múltiplo de 3:
print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

dato=int(input('Digite el número a verfificar si es múltiplo de 3: '))
if(dato%3==0):
    print('El número {} es múltiplo de 3'.format(dato))
else:
    print(f'El número: {dato} no es multiplo de 3')