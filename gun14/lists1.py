# -*- coding: utf-8 -*-
"""
list comprenensions sunlarin alternatifi: map + filter
hepsi icin, isin icine lambda(isimsiz, anonymous fonksiyon) giriyor.
"""

import random


def random_list(n):
    list1 = []
    for i in range(n):
        sayi = random.randint(1, 20)
        list1.append(sayi)
    return list1


def cift_mi(x):
    if x % 2 == 0:
        return True
    return False


def sonu_dort_mu(n):
    n_str = str(n)
    if n_str.endswith("4"):
        return True
    return False


def do_list_comp():
    list1 = random_list(12)
    # print(list1)
    list1 = [3, 16, 5, 14, 11, 4, 5, 8, 1, 4, 17, 17]

    # list copy
    list2 = list1[:]
    list2 = list1.copy()

    # list comp ile copy
    list3 = [sayi for sayi in list1]

    # cift sayilari secelim.
    list4 = [sayi for sayi in list1 if sayi % 2 == 0]
    # filter ile de yapilabilirdi.

    # cift sayilari, fonksiyon ile secelim.
    list4 = [sayi for sayi in list1 if cift_mi(sayi)]
    print(list4)
    # [16, 14, 4, 8, 4]

    list5 = [sayi for sayi in list1 if sonu_dort_mu(sayi)]
    print(list5)
    # [14, 4, 4]

    list6 = [sayi ** 2 for sayi in list1 if sayi >= 10 and sayi != 17]
    print(list1)
    print(list6)

    # sonu 4 ile biten sayilar.

    print()


def main():
    do_list_comp()


if __name__ == "__main__":
    main()
