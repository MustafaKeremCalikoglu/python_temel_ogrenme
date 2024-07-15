liste=["ahmet","mehmet","ali","veli","malik","mustafa"]

for i in range(4):
    print("gelemeyeceğin için üzgünüm"+" "+liste[0])
    print("---------------------")
    liste.pop(0)


print("listede geri kalanlar")
print(liste)
