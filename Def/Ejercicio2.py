import random
def adivi(aleatorio):
    numero=0
    while numero != aleatorio:
        numero=int(input("Ingrese el numero del 1 al 10:"))
        if numero> aleatorio:
            print("El numero ingresado es mayor al numero a adivinar")
        elif numero < aleatorio:
            print("El numero ingresado es menor al numero a adivinar")
        else:
            print("Felicidades adivinaste el numero",numero)
            
aleatorio= random.randint(1,10)
print (str (aleatorio))
adivi(aleatorio)