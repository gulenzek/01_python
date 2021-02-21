# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
Verilen bir listedeki elemanları topluyor.
"""


def listeyi_topla(liste):
    toplam = 0
    for eleman in liste:
        toplam += eleman
    return toplam


def iki_numaranin_buyugu(x, y: int):
    if x > y:
        return x
    return y


def uc_numaranin_en_buyugu(x, y, z: int):
    return iki_numaranin_buyugu(x, iki_numaranin_buyugu(y, z))


def listedeki_sayilari_carp(liste):
    carpim = 1
    for sayi in liste:
        carpim *= sayi
    return carpim


def yaziyi_tersten_oku(str1):
    ters_str = ""
    index = len(str1)
    while index > 0:
        ters_str += str1[index - 1]
        index = index - 1
    return ters_str


def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add


func = test(4)
print(func(4))


def main():
    print(listeyi_topla([1, -3, 9, 10, 30, -20]))
    print(uc_numaranin_en_buyugu(5, 6, 10))
    print(listedeki_sayilari_carp([1, -3, 9, 10, 5, 2]))
    print(yaziyi_tersten_oku("12345asbcd"))
    print(yaziyi_tersten_oku.__code__.co_nlocals)

    pass


if __name__ == "__main__":
    main()
