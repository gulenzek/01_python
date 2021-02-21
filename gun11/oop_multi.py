# -*- coding: utf-8 -*-
"""
oop_multi.py

      c1
c2          c3
      c4


       Kedigiller
Kaplan           Aslan
         Kedi

diamond problem


open for extension (yeni ozellikler katabilirsin)
closed for modification (ana amacini degistirme)
gelisime acik, degisime kapali.

Notifier
    SMSNotifier
    MailNotifier
    TwitterNotifier  # en cok begenilen yorumlari getirmesin.

"""

class Kedigiller:
    def agaca_tirman(self):
        print("Kedigiller")

    def tisla(self):
        pass

class Kaplan(Kedigiller):
    def agaca_tirman(self):
        print("Kaplan")

    def suda_yuz(self):
        pass

class Aslan(Kedigiller):
    def agaca_tirman(self):
        print("Aslan")

    def kirlarda_kostur(self):
        pass

class Kedi(Aslan, Kaplan, Kedigiller):
    pass

def main():
    kedi1 = Kedi()
    kedi1.agaca_tirman()  # Aslan
    # multiple inheritance destekleyen yeni bir dil ogrendiniz diyelim.
    # MRO: method resolution order ?

    kedi1.kirlarda_kostur()
    kedi1.suda_yuz()
    kedi1.tisla()


if __name__ == "__main__":
    main()
