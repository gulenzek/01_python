"""
oop_dortgen.py
"""


class Dortgen:
    """
        Dörtgen: diğer sınıfların atası olduğu için super veya base class olarak adlandırılır..
    """
    def __init__(self, en, boy):
        assert isinstance(en, (int, float))
        assert isinstance(boy, (int, float))
        self.en = en
        self.boy = boy

    def alan(self):
        return self.en * self.boy

    def cevre(self):
        return 2 * (self.en + self.boy)

    def __str__(self):
        # toString()
        return f"Dörtgen [{self.en}, {self.boy}]"

    def __len__(self):
        return self.cevre()

    def __repr__(self):


dortgen1 = Dortgen(5, 7)
print(dortgen1.alan())

print(dortgen1)

class Kare(Dortgen):
    def __init__(self, kenar):
        #
        #
        super().__init__(kenar, kenar)
    def __str__(self):
        pass

"""
oop_dortgen.py
"""

class Dortgen:
    """
    Dortgen, diger siniflarin atasi oldugu icin, buna super ya da base class denir.
    """
    def __init__(self, en, boy):
        assert isinstance(en, (int, float))
        assert isinstance(boy, (int, float))
        self.en = en
        self.boy = boy

    def alan(self):
        return self.en * self.boy

    def cevre(self):
        return 2 * (self.en + self.boy)

    def __str__(self):
        # toString()
        # bu user icin.
        return f"Dortgen [{self.en}, {self.boy}]"

    def __repr__(self):
        # representation, bu daha teknik, yazilim icin.
        return str(self)
        # return self.__str__()

    def __len__(self):
        # print(len(pk1))
        return self.cevre()

class Kare(Dortgen):
    def __init__(self, kenar):
        # super sinifin __init__() methodunu cagiralim.
        # yani Dortgen'in __init__() fonksiyonu cagirilir.
        super().__init__(kenar, kenar)

    def __str__(self):
        # override, eziyor.
        return super().__str__().replace("Dortgen", "Kare")
        # return f"Dortgen [{self.en}, {self.boy}]"

d1 = Dortgen(4, 5)
# Dortgen d1 = new Dortgen(4, 5);

# d1 = Dortgen("", "")
print(d1)

# callable: function ya da class.
k1 = Kare(3)
k2 = Kare(5)
alan2 = k2.alan()

print(k1)

k1.alan()

# encapsulation
# abstraction

a1 = d1.alan()
c1 = d1.cevre()

d2 = Dortgen(8, 9)
a2 = d2.cevre()

