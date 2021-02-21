"""
Dokümantasyon yazılıyor.
"""


class RenaultClio:
    def __init__(self, renk1, kapi_sayisi1):
        self.renk = renk1
        self.kapi_sayisi = kapi_sayisi1
        pass


    def display(self):
        print(self.renk, self.kapi_sayisi)


araba1 = RenaultClio("mavi", 4)
araba2 = RenaultClio("beyaz", 2)

araba1.display()


"""
# renault clio (class)
    # mavi, alihan
    # beyaz, mina

# vw golf (class)
    # gri, zeki
    # kirmizi, serdar
"""

s1 = "abc"  # __init__()

class RenaultClio:
    def __init__(self, renk1, kapi_sayisi1):
        self.renk = renk1
        self.kapi_sayisi = kapi_sayisi1

    def display(self):
        print(self.renk, self.kapi_sayisi)

# RenaultClio(araba1, "mavi", 4)  gibi yazmisiz gibi dusunebilirsiniz.
araba1 = RenaultClio("mavi", 4)
araba1.display()
# display(araba1)  gibi yazmisiz gibi dusunebilirsiniz.

araba2 = RenaultClio("beyaz", 2)
araba2.display()

s2 = "abc"
t1 = tuple([4, 5, 6])
t2 = (4, 5, 6)



