def mayordeedad (edad):
    bandera="false"
    if edad >= 18:
      bandera="True"
    return bandera
while True:
    dato= int (input("Ingrese su edad: "))
    if mayordeedad(dato)==True:
     print("Es mayor de edad")
     break
    else:
        print ("Menor de edad")