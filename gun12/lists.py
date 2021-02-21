# -*- coding: utf-8 -*-
"""
list comprehension, map, filter

GvR: list comprehension
map ve filter zaten vardi.
"""


class Kisi:
    def __init__(self, adi, boyu):
        self.adi = adi
        self.boyu = boyu
        self.formasi_var_mi = False

    def forma_ver(self):
        self.formasi_var_mi = True
        return self

    def __repr__(self):
        return f"{self.adi} {self.boyu} {self.formasi_var_mi}"


def main():
    k1 = Kisi("ahmet", 198)
    k2 = Kisi("fatma", 180)
    k3 = Kisi("tuncay", 168)

    # hangileri basketbolcu adayi olsun?
    # boyu 175 ustunu secelim.
    aday_adaylari = [k1, k2, k3]
    aday_adaylari2 = [x for x in aday_adaylari]  # kopyasi

    # eleman secme
    basketbolcu_adaylari = [kisi for kisi in aday_adaylari if kisi.boyu > 175]

    # eleman degistirme
    basketbolcu_adaylari2 = [kisi.forma_ver() for kisi in basketbolcu_adaylari]

    list1 = [100, 200, 300]
    list2 = [x for x in list1]  # kopya
    list3 = [x for x in list1 if x > 199]  # eleman secme  (filter yerine)
    list4 = [x + 2 for x in list1]  # eleman degistirme  (map yerine)

    def greater_than_199_old1(n):
        if n > 199:
            return True
        return False

    def greater_than_199_old2(n):
        return True if n > 199 else False

    def greater_than_199(n):
        return n > 199

    def add_2(n):
        return n + 2

    list3a = filter(greater_than_199, list1)  # filter object
    list3b = list(filter(greater_than_199, list1))  # list
    list3c = list(filter(lambda n: n > 199, list1))  # list

    list4a = map(add_2, list1)  # map object
    list4b = list(map(add_2, list1))  # list
    list4c = list(map(lambda z: z + 2, list1))  # list

    takimlar = ["england", "scotland", "wales"]
    puanlar = ["18", "22", "13"]
    zipped = zip(takimlar, puanlar)  # zip object
    zipped2 = list(zip(takimlar, puanlar))

    print()


if __name__ == "__main__":
    main()
