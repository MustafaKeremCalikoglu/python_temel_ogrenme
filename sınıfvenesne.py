"""
class Ogrenciler:
    isim="mustafa"
    okul="lise"
    numara="10"

print(Ogrenciler.isim)
print(Ogrenciler.okul)
print(Ogrenciler.numara)


talebe1=Ogrenciler()
print(talebe1.isim)
talebe1.isim="kerem"
print(talebe1.isim)


"""
"""
class Ogrenciler:
    def __init__(self,isim,numara):
        self.isim=isim
        self.numara=numara

talebe1=Ogrenciler("ali",15)
print(talebe1.isim)
print(talebe1.numara)

"""
class Ogrenciler:
    def __init__(self,isim,numara):
        self.isim=isim
        self.numara=numara
    def goster(self):
        return("öğrenci ismi"+self.isim)


"""
o1=Ogrenciler("ali","18")
print(o1.goster())
"""




















