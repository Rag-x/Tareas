alumnos={}
alumnos=dict()
alumnos={"0106663792":"Juan Bravo",
         "0107050270":"Antoni Mejia",
         "1501095408":"Pizango Jhordan",
         "0105410211":"Christian Preciado",
         "0106605017":"Astudullo Carlos",
         "0106767007":"Bruce",
         "0105737365":"Stallin Barbecho",
         "0954337572":"Torres Melanie ",
         "0106637150":"Paredes Jennifer",
         "0150564078":"Danny Alex",
         "0105041982":"Adrian Piña",
         "0106399041":"Jacqueline Tenesaca",
         "0150474021":"David Ñauta",
         "0107270282":"Edwin Arroyo",
         "0107416927":"Jose Muñoz",
         "0150578094":"Nayeli Gallegos",
         }
alumnos["0107359788"]="Ariel Villa"
alumnos["1105050755"]="Veronica Chombo"
print (alumnos)
print(alumnos["0954337572"])
print(alumnos.get("0954337572","No se encuentra en el diccionario"))
alumnos.pop("0954337572")
print(alumnos)
print(alumnos.get("0954337572","No se encuentra en el diccionario"))
for e in alumnos.keys():
    print(e)
for e in alumnos.values():
    print(e)
for e in alumnos.items():
 print("la llave y el valor es:",e) 
