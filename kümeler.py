
s="ankara"
d=set(s)    # kümeye çevirdim
print(d)

liste=[1,2,3]
c=set(liste)
print(c)
print(type(c))


a={1,2,3}
b={3,4,5}
print(a|b) #birleşim
print(a&b)  #kesişim
print(a-b)  #fark
print(a^b) #simetrik fark


#METOTLAR
r={10,11,12,13}


r.add(100)  #ekleme

e=r.copy()
print(e)

r.discard(10)   #silme
print(r)

r.remove(11)  #silme
print(r)





print(a.union(b))	#birleştirme

print(a.intersection(b))  #kesişim

print(a.difference(b))	 	#fark

print(a.symmetric_difference(b))		#simetrik fark

print(a.issubset(b))  # a b'nin alt kümesimi

print(3 in(a))  #içindemi




#donuk kümeler   (frozenset )

p=[1,2,3,4,5]
f=frozenset(p)
print(f)
print(type(f))
print(dir(f))




























