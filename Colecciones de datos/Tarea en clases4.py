elementos=[0,1,-1,0,5,-2,-6,8,10,9,-3,-5,-10,0]
ceros=[]
positivos=[]
negativos=[]

for e in elementos:
    if e == 0:
       ceros.append(e)
       
    elif e > 0: 
        positivos.append (e)
    elif e < 0 :
        negativos.append (e)
print (ceros)
print (positivos)
print (negativos)

