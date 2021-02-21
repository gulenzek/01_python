# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
Q5 random olarak strong password olusturan bir fonksiyon yazınız.
random modulunden faydalanabilirsiniz.

Random strong password..
"""
import random

KARAKTERLER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I',
               'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q',
               'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
               '~', '>', '*', '(', ')', '<&#']


def random_strong_password(karakter_uzunlugu):
    sonuc = ""
    for i in range(karakter_uzunlugu):
        sonuc = sonuc + random.choice(KARAKTERLER)
    return sonuc


def main():
    while True:
        sifre_uzunlugu = int(input(">>>"))
        print(str(random_strong_password(sifre_uzunlugu)))
        print('<&#')
    pass


if __name__ == "__main__":
    main()
