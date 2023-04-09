alumnos = {"Juan": {"edad": 22, "promedio": 8.5}, "Maria": {"edad": 20, "promedio": 9.0}, "Pedro": {"edad": 25, "promedio": 7.5}}
for e in alumnos: 
 print (e)
for c,v in alumnos.items():
    print (c,v)
for e in alumnos.items():
  if e == 20 and e == 22:
      print (e)