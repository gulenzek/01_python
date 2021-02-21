# -*- coding: utf-8 -*-
"""
oop_inheritance.py

bir str sinifimiz olsun.
icinde, middlestrip() olsun.
"""

class Kedigil:
    def agaca_tirman(self):
        pass

class Kedi(Kedigil):
    pass

class Str2(str):
    # how to extend Python built-in class?

    # def __init__(self, str1):
    #     super().__init__()

    def middlestrip(self):
        # TODO: sonradan duzgun implementasyonunu yap.
        return self.replace(" ", "")

# kurucu, olusturucu, yapici, constructor

def main():
    kedi1 = Kedi()
    kedi1.agaca_tirman()  # atasindan geldi.
    s2 = Str2("  ab c ")
    metin = s2.middlestrip()
    print(metin)

if __name__ == "__main__":
    main()
