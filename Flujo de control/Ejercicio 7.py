# 7 La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#- Ingredientes vegetarianos: Pimiento y tofu.
#- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
#respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede 
#eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por
#pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n1)- Vegetariana\n2)- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: ")

if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n1)- Pimiento\n2)- Tofu\n")
    ing = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ")
    if ing == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n1)- Peperoni\n2)- Jamón\n3)- Salmón\n")
    ing = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ")
    if ing == "1":
        print("peperoni")
    elif ing == "2":
        print("jamón")
    else:
        print("salmón")