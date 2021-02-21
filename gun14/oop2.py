# -*- coding: utf-8 -*-
"""

"""


class ElektronikCihaz:
    def prize_tak(self):
        pass

    def ac(self):
        pass

    def kapat(self):
        pass


class Bilgisayar(ElektronikCihaz):
    def oyun_oyna(self):
        print("Bilgisayarda oyun oyna")


class TusluTelefon(ElektronikCihaz):
    def oyun_oyna(self):
        print("Tuslu telefonda oyun oyna (snake)")

    def ara(self):
        pass


class AkilliTelefon(TusluTelefon, Bilgisayar):
    def oyun_oyna(self):
        # polymorphism
        print("iPhone'da oyun oyna (snake)")


def main():
    iphone12 = AkilliTelefon()
    iphone12.oyun_oyna()  # Bilgisayarda
    # MRO: method resolution order

    nokia8110 = TusluTelefon()
    nokia8110.oyun_oyna()  # Tuslu telefonda oyun oyna (snake)


if __name__ == "__main__":
    main()
