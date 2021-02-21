# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
The greatest common divisor is here!
"""


def main():
    m = int(input("Lütfen bir sayı giriniz:"))
    n = int(input("Lütfen bir sayı giriniz:"))
    d = min(m, n)

    while True:
        if m % d != 0 or n % d != 0:
            d -= 1
        elif m % d == 0 and n % d == 0:
            print("En büyük ortak bölen {} sayısıdır.".format(d))
            break

    pass


if __name__ == "__main__":
    main()
