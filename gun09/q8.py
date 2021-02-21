# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
Bir liste sıralı mı?
Bir listeyi parametre olarak alan, liste zaten sıralı ise True, değilse False
donduren bir fonksiyon yazınız.

"""


def liste_sirali_mi(liste):
    sonuc = False
    if liste.sort():
        sonuc = True
    return sonuc

def main():

    print(liste_sirali_mi([1,5,7,9]))
    pass


if __name__ == "__main__":
    main()
