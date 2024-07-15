class ebeveny:
    def __init__(self,isim,memleket):
        self.isim=isim
        self.memleket=memleket
    def goster(self):
        print("adım ",self.isim," ve memleket ",self.memleket )

class cocuk(ebeveny):
      pass


c1=cocuk("ali","izmir")
c1.goster()
