#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE LISTAS A RESOLVER
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
num=[]
for e in range(1, 6):
 num.append(e)
print("Lista de números del 1 al 5:", num) 

#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
nom = ['Juan','Jose','David','Jonathan','Pedro','Maria','Eduardo','Fernado','Jenifer']
nom1= nom[0]
print ("El primer nombre es:",nom1)

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
nume=[1,2,3,4,5,6,7,8,9,10]
for e in nume:
    if e%2 == 0 :
        print ("Los sigientes numeros son pares:",e)
        
#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
nom = ['Juan','Jose','David','Jonathan','Pedro','Maria','Eduardo','Fernado','Jenifer']
nom1= nom[-1]
print ("El primer nombre es:",nom1)

#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
nume=[1,2,3,4,5,6,7,8,9,10]
me= nume[-1]
print ("El ultimo elemento es:",me)

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
nume=[1,2,3,4,5,6,7,8,9,10]
for e in nume:
    if e%2 != 0 :
        print ("Los sigientes numeros son impares:",e)
        
#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
nom = ['Juan','Jose','David','Jonathan','Pedro','Maria','Eduardo','Fernado','Jenifer']
ned = "Jonas"
nom.insert(2,"Eduardo")
nom.append(ned)
print (nom)

#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
nume=[1,2,3,4,5,6,7,8,9,10]
me= nume[0]
ma= nume [-1]
print ("El primer elemento es: ",me," y el ultimo elemento es: ",ma)

#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
nom = ['Juan','Jose','David','Jonathan','Pedro','Maria','Eduardo','Fernado','Jenifer']
n = len(nom) 
print ("el numero de elementos de la lista es:",n)

#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
nume=[1,2,3,4,5,6,7,8,9,10]
#Otro metodo:
#suma=0
#for e in nume:
#suma+=e
#print(suma)
m=sum(nume)
print ("la suma de la lista es:", m)