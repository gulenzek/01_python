# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
getsetitem.py
"""


class Ucak:
    def __init__(self):
        self._yolcular = {}

    def yolcu_ekle(self, koltuk, yolcu):
        self._yolcular[koltuk] = yolcu

    def __setitem__(self, key, value):
        self._yolcular[key] = value

    def __getitem__(self, item):
        return self._yolcular[item]


def main():
    u1 = Ucak()

    u1["A8"] = "Ahmet"
    u1["A9"] = "Aysun"
    u1["C1"] = "Fatma"

    print(u1["A9"])
    pass


if __name__ == "__main__":
    main()
