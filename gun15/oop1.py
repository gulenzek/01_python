# -*- coding: utf-8 -*-
"""

"""

class AkilliTelefon:
    def __init__(self, renk, agirlik):
        self.renk = renk
        self.agirlik = agirlik

    def boya(self, renk):
        self.renk = renk

    def caldir(self):
        # TypeError: caldir() takes 0 positional arguments but 1 was given
        pass

    @staticmethod
    def ithal_et(model, kac_tane):
        # AkilliTelefon.ithal_et("iphone12", 100)
        pass

    @classmethod
    def ihrac_et(cls, model, kac_tane):
        # cls: AkilliTelefon
        # AkilliTelefon.ihrac_et("iphone12", 100)
        pass

    def __add__(self, other):
        # yeni_telefon = AkilliTelefon()
        # return yeni_telefon
        return self


def main():
    adilin_telefonu = AkilliTelefon("siyah", 180)  # 100, self: adilin_telefonu
    minanin_telefonu = AkilliTelefon("mor", 150)  # 200, self: minanin_telefonu

    adilin_telefonu.boya("kirmizi")
    # boya(adilin_telefonu, "kirmizi")
    adilin_telefonu.caldir()
    # caldir(adilin_telefonunu)

    # NFC:
    adilin_telefonu = adilin_telefonu + minanin_telefonu
    # boyle dusunebiliriz: adilin_telefonu.__add__(minanin_telefonu)


if __name__ == "__main__":
    main()
