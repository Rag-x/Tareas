print ("Nombre: Juan Bravo")
print ("Curso: Fundamentos de Python")
print ("Fecha: 30/3/2023")

nota=float(input("Ingrese la nota: "))
if nota >= 0 and nota <= 2:
    print(f"La nota de {nota} es muy deficiente")
elif nota >= 3 and nota <= 4:
    print(f"La nota de {nota} es insuficiente")
elif nota >= 5 and nota <= 6:
    print(f"La nota de {nota} es suficiente")
elif nota == 7:
    print(f"La nota de {nota} esta bien")
elif nota >= 8 and nota <= 9:
    print(f"La nota de {nota} es notable")
elif nota == 10:
    print(f"La nota de {nota} es sobresaliente")
else:
    print(f"La nota de {nota} no existe")
