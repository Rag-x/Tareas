#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla de números enteros y calcular su suma y promedio.
tupla=(1,2,3,4,5)
suma=sum(tupla)
print ("El total de la suma es:",suma)
promedio=suma/len(tupla)
print("El promedio es:",promedio)
#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
suma = tuple(map(sum, zip(tup1, tup2)))
print("La tupla resultante es:", suma)
#Crear una tupla de nombres y ordenarla alfabéticamente.
nombres = ("Juan", "Pedor", "Jose", "Mario", "Eunis","Alberto")
nom= sorted(nombres)
n=tuple(nom)
print("El orben alfabetico es:", n)

#Crear una tupla de números y encontrar el valor mínimo y máximo.
num=(1,2,3,4,5,6,7,8,9)
print("Numero minimo de la tupla:",min (tupla))
print("Numero maximo de la tupla:",max (tupla))
#Crear una tupla de números y convertirla en una lista.
num= (1, 2, 3, 4, 5)
nume = list(num)
print("La tupla convertida en lista es:", nume)
#Crear una tupla con los días de la semana y mostrar el tercer elemento.
dias = ("Lunes", "Martes", "Miercoles", "Jueves" ,"Viernes", "Sabado", "Domingo")
ter = dias[2]
print("El tercer día de la semana es:", ter)

#Crear una tupla con números enteros y mostrar aquellos que son pares.
numer = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
pares = tuple(filter(lambda x: x % 2 == 0, numer))
print("Los números pares son:", pares)
#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
mas = tuple(filter(lambda x: len(x) > 5, meses))
print('Los meses con más de cinco letras son:', mas)
#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
edades = (11, 23, 16, 19, 30, 18, 22, 27, 10)
mayores = len(tuple(filter(lambda x: x > 18, edades)))
print("La cantidad", mayores)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
libros = (
    ("Estadistica", "Mario.F", 2009),
    ("La Odisea", "Homero", -800),
    ("El dia que dios entro al banco", "Juan Gomez", 1967)
)
titulo = libros[2][0]
print('El título del tercer libro es:', titulo)

