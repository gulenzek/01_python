# -*- coding: utf-8 -*-
"""
oop_getitem.py
Python: getitem/setitem
C#: indexer
Java: karsiligi yok.
"""

class Otobus:
    def __init__(self):
        self._koltuklar = {}

    def bilet_al(self, koltuk_no, tc_kimlik_no):
        # TODO: validasyon
        self._koltuklar[koltuk_no] = tc_kimlik_no

    def koltukta_kim_var(self, koltuk_no):
        return self._koltuklar.get(koltuk_no, None)

    def __setitem__(self, key, value):
        self.bilet_al(koltuk_no=key, tc_kimlik_no=value)

    def __getitem__(self, item):
        return self.koltukta_kim_var(koltuk_no=item)

    # DRY: don't repeat yorself

def main():
    bus1 = Otobus()
    bus1.bilet_al("A3", "tc100")

    # bunu, __setitem__() sagliyor:
    bus1["A4"] = "tc101"
    # bus1[key] = value
    print(bus1["A4"])  # tc101
    print(bus1["A5"])  # None

    list1 = ["a", "b", "c"]
    tuple1 = ["a", "b", "c"]
    print(tuple1[1])
    # [] -> indexing operator


if __name__ == "__main__":
    main()
