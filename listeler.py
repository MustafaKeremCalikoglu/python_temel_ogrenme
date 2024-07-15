liste=["kerem",10,True,[1,2,3]]
x=[1,2]
print(liste[1:3])
print(len(liste))

print(liste[3][2])
print(x+liste)

print(10 in liste)


liste[0]="papatya"

print(liste)


isimler=["ali","veli","ayşe"]
maaslar=[2000,5000,4000]
isimler.append("mert")
#isimler.extend(maaslar)
print(isimler)

isimler.insert(0,"mustafa")
print(isimler)

print(isimler.index("mustafa"))

isimler.sort()
print(isimler)
maaslar.sort()
print(maaslar)

isimler.reverse()
print(isimler)

isimler.remove("ali")
print(isimler)

isimler.pop(2)
print(isimler)




















