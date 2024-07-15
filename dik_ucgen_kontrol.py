
# mustafa kerem çalıkoğlu 20120101059


sayi_listesi=[]

sayi1=int(input("ilk sayiyi giriniz:  "))
sayi2=int(input("ikinci sayiyi giriniz:  "))
sayi3=int(input("üçüncü sayiyi giriniz:  "))

sayi_listesi.append(sayi1)
sayi_listesi.append(sayi2)
sayi_listesi.append(sayi3)

sayi_listesi.sort(reverse=True)

if (sayi_listesi[0] ** 2 ) == ( sayi_listesi[1] ** 2) +  ( sayi_listesi[2] ** 2 ):
    print("------------------")
    print("dik ucgen olusturulabilir")
else:
    print("------------------")
    print("dik ucgen olusturulamaz")    


