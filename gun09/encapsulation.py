# encapsulation.py
# kapsullemek.

class DikDortgen:
    def __init__(self, en, boy):
        # self._en = en  # protected
        # self._boy = boy  # protected
        self.__en = en  # private
        self.__boy = boy  # private
        self.cevre = None  # public

    def __get_en(self):
        return self.__en

    def __set_en(self, yeni_en):
        self.__en = yeni_en
        self.cevre_hesapla()

    enx = property(__get_en, __set_en, None, None)

    def cevre_hesapla(self):
        self.cevre = self.__en * self.__boy


d1 = DikDortgen(3, 5)
d1.cevre_hesapla()
print(d1.cevre)
d1.set_en(8)
print(d1.cevre)
d1.enx = 9
x = d1.enx

d1.enx = 7
cevre = d1.cevre



#
#
#

# encapsulation.py
# kapsullemek.

class DikDortgen:
    def __init__(self, en, boy):
        # self._en = en  # protected
        # self._boy = boy  # protected
        self.__en = en  # private
        self.__boy = boy  # private
        self.__cevre = None  # public
        self.__cevre_hesapla()

    # BEGIN builtin property kullanarak
    def __get_en(self):
        return self.__en

    def __set_en(self, yeni_en):
        self.__en = yeni_en
        self.__cevre_hesapla()

    en = property(__get_en, __set_en, None, None)
    # END builtin property kullanarak

    # BEGIN property decorator kullanarak
    @property
    def boy(self):
        return self.__boy

    @boy.setter
    def boy(self, value):
        self.__boy = value
        self.__cevre_hesapla()
    # END property decorator kullanarak

    def __cevre_hesapla(self):
        self.__cevre = self.__en * self.__boy

    @property
    def cevre(self):
        return self.__cevre


d1 = DikDortgen(3, 5)
print(d1.cevre)  # 3*5 = 15

d1.en = 9
x = d1.en
print(d1.cevre)  # 9*5 = 45

print(dir(d1))
# d1.__cevre_hesapla()
# private elemanlara erisim:
d1._DikDortgen__cevre_hesapla()

# tutarliligi bozar:
d1._DikDortgen__cevre = 49

