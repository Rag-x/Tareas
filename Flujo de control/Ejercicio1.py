print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")
print ("Estados del semaforo /rojo/amarillo/verde")
semaf=input("Estado del color del semaforo: ")
if semaf=="rojo":
    print ("La persona no crusar")
elif semaf=="amarillo":
    print("La persona no puede crusar")
elif semaf=="verde":
    print("La persona puede crusar")
else :
    print("No corresponde a un estado del semaforo")