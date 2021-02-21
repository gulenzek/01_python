# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
BankAccount isimli bir sınıf oluşturuldu.
Bakiye alındı. Bakiye verilmediğinde 0 lira ile başlatıldı.
para_yatir, para_cek fonksiyonları yazıldı.
Bakiyeyi kendisi hesaplıyor.
Bakiyeyi dışarıya göstermek için miktar_goster() fonksiyonu yazıldı.
Hesap hareketlerini gösteriyor ve miktar_goster() fonksiyonu ile 

"""


class BankAccount:
    log = []
    miktar = 0.0

    def __init__(self, baslangic_bakiyesi=0.0):
        self.bakiye = baslangic_bakiyesi
        self.log = self.log + ["Banka hesabı {} lira ile yaratıldı.".format(baslangic_bakiyesi)]

    def __str__(self):
        self.log = self.log + ["Banka hesabı {} lira ile görüntülendi.".format(self.bakiye)]
        return "Bu bir banka hesabıdır ve bakiyesi {} liradır.".format(self.bakiye)

    def para_yatir(self, miktar):
        self.log = self.log + ["Banka hesabına {} lira para yatırıldı.".format(miktar)]
        self.bakiye = self.bakiye + miktar

    def para_cek(self, miktar):
        self.log = self.log + ["Banka hesabından {} lira para çekildi.".format(miktar)]
        self.bakiye = self.bakiye - miktar

    def miktar_goster(self):
        self.log = self.log + ["Banka hesabı {} lira bakiye ile gösterildi.".format(self.bakiye)]
        bakiye = "Banka hesabında {} lira vardır.".format(self.bakiye)
        return bakiye

    def log_goster(self, numara):
        return self.log[numara]



def main():
    hesap1 = BankAccount(10000)
    print(hesap1)
    hesap1.para_yatir(200)
    print(hesap1)
    hesap1.para_cek(400)
    hesap1.para_yatir(350.5)
    print(hesap1)
    print(hesap1.miktar_goster())

    loglar = hesap1.log
    for i in loglar:
        print(i)


    pass


if __name__ == "__main__":
    main()
