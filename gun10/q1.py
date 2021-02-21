# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
q1 sezar sifreleme methodunu yazınız:
def sezar_sifrele(kaydirilacak_harf_sayisi, acik_metin):
    pass
"""


def sezar_sifrele(sayi: int, raw_metin):
    """
    Sezar şifrelemesi metodu.
    Alfabede yer alan karakterlerin indeksini verilen sayı kadar öteleyip denk gelen karakteri yazıyor.
    Alfabede bulamadığı karakterleri ise olduğu şekilde yazıyor.
    """
    sifreli_metin = ""
    alfabe = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    for i in raw_metin:
        if i not in alfabe:
            sifreli_metin += i
        else:
            sifreli_metin += alfabe[(alfabe.index(i) + sayi) % len(alfabe)]

    return sifreli_metin


def main():
    print(sezar_sifrele(5, "Merhaba zeki gülen abc"))
    pass


if __name__ == "__main__":
    main()
