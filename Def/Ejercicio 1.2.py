def contadorAsendente(num):
    cadena=""
    cont = 0    
    while cont <= num:
        cadena+=str(cont)
        cont+=1
    return cadena   
def contadorDescendente(num):
    cadena = ""
    
    while num>= 0:
        cadena += str(num)
        num -= 1
    return cadena  
num =int(input("Ingrese un numero: "))
print(contadorAsendente(num))
print(contadorDescendente(num))