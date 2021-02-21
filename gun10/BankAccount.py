# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""


class BankAccount:
    def __init__(self, baslangic_bakiyesi=0.0):
        self.bakiye = baslangic_bakiyesi
        self.log = self.log + ["Banka hesabı {} lira ile yaratıldı.".format(baslangic_bakiyesi)]

    def __str__(self):
        self.log = self.log



def main():
    hesap1 = BankAccount(100)
    print(hesap1)
    pass


if __name__ == "__main__":
    main()
