a=set()
a.add(1)
a.add(3)
a.add(6)
a.add(5)
a.add(4)
print ("Conjunto A",a)
b=set()
b.add(3)
b.add(5)
b.add(6)
b.add(4)
b.add(8)
b.add(10)
print ("Conjunto B",b)
c=set()
c.add(3)
c.add(5)
c.add(9)
print ("Conjunto C",c)
b.discard (8)
print("Conjunto B",b)
d=a.copy()
print ("Conjunto D",d)
c.clear()
print ("Conjunto C",c)
c=b.copy()
print ("Conjunto C",c)
print(c.isdisjoint(b))
e=set()
e.add(3)
e.add(4)
print(e.issubset(b))
print(e.issubset(a))
print(e.issubset(d))
print(e.issuperset(c))
f=c.union(b)
print ("Cunjunto F",f)
a.update(b)
print ("Cunjunto A",a)
print(a.difference(b))
a.difference_update(b)
print("Conjunto A",a)
print(c.intersection(b))
c.intersection_update(d)
print("Conjunto A:",a)
print("Conjunto B:",b)
print("Conjunto C:",c)
print("Conjunto D:",d)
print("Conjunto E:",e)
print("Conjunto f:",f)
print(c.symmetric_difference(d))