# listeden farklı olarak demetlerin elemanları değiştirilemez


kordinatlar=(1,2,3)
x,y,z=kordinatlar
print(x,y,z)


x=(1,2,3,["mustafa",1907])
print(type(x))
print(len(x))
x[3][1]=1903
print(x)
#demtlerin içindeki listedeki değeri değiştirebilirsiniz demetler içindeki listelere karışmaz


