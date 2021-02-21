from oop_dortgen import Dortgen


class ParalelKenar(Dortgen):
    def __init__(self, en, boy, yukseklik):
        super().__init__(en, boy)
        self.yukseklik = yukseklik

    def alan(self):
        return self.boy * self.yukseklik


pk = ParalelKenar(12, 24, 5)

print(pk.cevre())


# paralelkenar.py
# Dortgen'den inherit ederek yapalim.

# https://repl.it/@caglartoklu/SiemensPythonEgitimiGun09

# paralelkenar.py
# Dortgen'den inherit ederek yapalım.

from oop_dortgen import Dortgen
from oop_dortgen import Kare


class ParalelKenar(Dortgen):
    def __init__(self, en, boy, yukseklik):
        # super() :super sinifin __init__() mwethodunu cagirir.
        super().__init__(en, boy)
        self.yukseklik = yukseklik

    def alan(self):
        return self.en * self.yukseklik

    def __str__(self):
        # override ,eziyor.
        return super().__str__().replace("Dortgen", "ParalelKenar")


pk1 = ParalelKenar(2, 5, 3)
print(pk1.alan())  # 6
# print(pk1.pk_alan())  # 6
print(pk1.cevre())  # 14
print(len(pk1), "len")  # 14

# inheritance(miras) cevre() methodu, mirsa olarak geldi.
# alan() methodu bu class icin ugyn degil.
# override etmem gerekti.
# bu durumda, polymorphism(cok bicimlilik) prensibini uyduladik.

k1 = Kare(6)
x = k1.alan()
