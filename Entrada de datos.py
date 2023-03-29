x=int(input("Introducir el numero: "))
y=int(input("Introducir el numero: "))
#1
num =x == y
print("Los numeros: "+str(x)+" y " +str(y)+" son iguales: " + str (num))
print(f"Los numeros: {x} y  {y}  son iguales: {num} ")
print("Los numeros: {} y {} son iguales: {}".format (x,y, num))
print("Los numeros: ",x," y ",y, " son iguales: ",num,"\n")
#2
num =x!= y
print("Los numeros: "+str(x)+" y " +str(y)+" son diferentes: " + str (num))
print(f"Los numeros: {x} y  {y}  son diferentes: {num} ")
print("Los numeros: {} y {} son diferentes: {}".format (x,y, num))
print("Los numeros: ",x," y ",y, " son diferentes: ",num,"\n")
#3
num =x>y
print("Los numeros: "+str(x)+" y " +str(y)+" El primero es mayor: " + str (num))
print(f"Los numeros: {x} y  {y}  El primero es mayor: {num} ")
print("Los numeros: {} y {} El primero es mayor: {}".format (x,y, num))
print("Los numeros: ",x," y ",y, " El primero es mayor: ",num,"\n")
#4
num =x <= y
print("Los numeros: "+str(x)+" y " +str(y)+" es mayor o igual: " + str (num))
print(f"Los numeros: {x} y  {y}  es mayor o igual: {num} ")
print("Los numeros: {} y {} es mayor o igual: {}".format (x,y, num))
print("Los numeros: ",x," y ",y, " es mayor o igual: ",num,"\n")
############################################################
non=input("Cual es tu nombre: ") 
print("!Hola" + str (non),"¡")
print(f"!Hola {non} ","¡")
print("!Hola {}".format (non),"¡")
print("!Hola",non,"¡","\n")