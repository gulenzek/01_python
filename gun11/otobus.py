# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
DRY: Don't Repeat Yourself

"""


class Otobus:
    def __init__(self):
        self._koltuklar = {}

    def bilet_al(self, koltuk_no, tc_kimlik_no):
        # TODO validation
        self._koltuklar[koltuk_no] = tc_kimlik_no

    def koltukta_kim_var(self, koltuk_no):
        return self._koltuklar.get(koltuk_no, None)

    def __setitem__(self, key, value):
        self.bilet_al(koltuk_no=key, tc_kimlik_no=value)

    def __getitem__(self, item):
        return self.koltukta_kim_var(koltuk_no=item)


def main():
    bus1 = Otobus()
    bus1.bilet_al("A12", 22238729987)

    bus1["A11"] = 12323434545
    bus1["A12"] = 29009823498

    print(bus1["A11"])
    print(bus1["A12"])
    bus1["A12"] = "23434545678"
    print(bus1["A12"])
    print(bus1["A11"])

    print(bus1)

    pass


if __name__ == "__main__":
    main()
