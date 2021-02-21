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
    pass


def main():
    iphone12 = AkilliTelefon()
    iphone12.oyun_oyna()  # Bilgisayarda


if __name__ == "__main__":
    main()
