def contadorAsendente(num):
    cadena=""
    cont = 0    
    while cont <= num:
        cadena+=str(cont)
        cont+=1
    return cadena     
def contadordesendente(num):
    cadena=""
    cont =num
    while cont >=0:
        cont-=1
    return cadena 
num =int(input("Ingrese un numero: "))
print(contadorAsendente(num))
print(contadordesendente(num))


        