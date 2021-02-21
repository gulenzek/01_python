# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
herhangi bir password (yani string) "strong" mu değil mi, buna göre True/False donduren bir fonksiyon yazınız.
Strong olma durumu da şöyle olsun diyelim:
en az 8 uzunluk.
En az 2 rakam
En az bir noktalama isareti
En az 2 büyük harf
string fonksiyonlari dokumanı:
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

"""
import string


def sayi_uzun_mu(sifre):
    sonuc = 0
    for karakter in sifre:
        if str(karakter).isdigit():
            sonuc += 1
    if sonuc >= 2:
        return True
    else:
        return False


def noktalama_uzun_mu(sifre):
    sonuc = 0
    for karakter in sifre:
        if karakter in string.punctuation:
            sonuc += 1
    if sonuc >= 1:
        return True
    else:
        return False


def buyuk_harf_uzun_mu(sifre):
    sonuc = 0
    buyuk_harfler = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P",
                     "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]
    for karakter in sifre:
        if karakter in buyuk_harfler:
            sonuc += 1
            continue
    if sonuc >= 2:
        return True
    else:
        return False


def guclu_mu(sifre):
    # uzunluk >= 8
    # sayi >= 2
    # noktalama >=1
    # büyükharf >= 2 olmalı
    sayi_uzunluk = sayi_uzun_mu(sifre)
    noktalama_uzunluk = noktalama_uzun_mu(sifre)
    buyuk_harf_uzunluk = buyuk_harf_uzun_mu(sifre)
    sonuc = False
    if len(sifre) >= 8:  # >= 8
        if sayi_uzunluk:
            if noktalama_uzunluk:
                if buyuk_harf_uzunluk:
                    sonuc = True
    return sonuc


sifre = input(">>>")
print(guclu_mu(sifre))


def main():
    pass


if __name__ == "__main__":
    main()
