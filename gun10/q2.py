# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""
import datetime
class ShoppingCalculator(object):
    def __init__(self, budget=0.0, toplam_harcama=0.0, sepet=None):
        self.is_under_budget = True
        assert isinstance(budget, (float, int))
        if budget < 0:
            print("bütçenin altındaki yer..")
        else:
            self.__budget = budget

        self.sepet = sepet
        self.toplam_harcama = toplam_harcama

        self.sepet = []
        self.log = []
        self.log += [str(datetime.datetime.now()) + " - " + "Alışverişe {} lira miktar ile başlandı.".format(budget)]

    @property
    def budget(self):
        return self.__budget

    def add_budget(self, budget):
        self.__budget += budget
        self.log += [str(datetime.datetime.now()) + " - " + "Alışveriş miktarı {} lira artırıldı.".format(budget)]
        return self.budget

    def buy(self, urun, kategori, birim_fiyat, adet):
        self.sepet = [urun, kategori, birim_fiyat, adet, (birim_fiyat * adet)]
        self.toplam_harcama += (birim_fiyat * adet)
        self.log += [str(datetime.datetime.now()) + " - " + "Alışveriş miktarı {} lira harcandı.".format((birim_fiyat * adet))]
        return 1

    def is_under_budget(self):
        self.is_under_budget = True
        if self.__budget < self.sepet: # burayı anlamadım..
            self.is_under_budget = False
        else:
            pass
        return self.is_under_budget

    pass

    def remaining_budget(self):
        remaining_budget = self.__budget - sum(self.sepet)
        return remaining_budget


def main():
    sc1 = ShoppingCalculator(300)
    sc1.add_budget(100)
    sc1.buy("domates", "gida", 3, 3.5)
    sc1.buy("patates","gıda", 4, 4.5)
    sc1.buy("deterjan", "temizlik", 20, 4)
    sc1.buy("sabun", "temizlik", 10, 5)

    loglar = sc1.log
    for i in loglar:
        print(i)
    print(sc1.toplam_harcama)
    print(sc1.is_under_budget)

    print(sc1.remaining_budget())
#  # surucu(driver) kodu:
#  shopping1 = ShoppingCalculator(300)  # bütçe olarak 300 TL'miz var.
#  shopping1.add_budget(100)  # 100 daha geldi.
#
#  # ürün adı, kategori, birim fiyat, kaç tane
#  shopping1.buy("domates", "gida", 20, 1)
#
#  # ürün adı, kategori, birim fiyat, kaç tane.
#  # aşağıda, birimden 2 tane almisiz, yani 15*2=30 TL harcama olacak.
#  shopping1.buy("patates", "gida", 15, 2)
#
#  shopping1.buy("deterjan", "temizlik", 20, 2)
#  shopping1.buy("sabun", "temizlik", 40, 2)
#
#  print(shopping1.is_under_budget())  # bütçe dahilinde miyiz?
#  print(shopping1.total_spent)  # toplamda kaç TL harcadik?
#  print(shopping1.remaining)  # toplamda kaç TL butcemiz kaldı?
#
#  shopping1.buy("elektronik", "playstation 4", 3500, 1)
#
#  print(shopping1.is_under_budget())  # bütçe dahilinde miyiz?
#  print(shopping1.total_spent)  # toplamda kaç TL harcadik?
#  print(shopping1.remaining)  # toplamda kaç TL butcemiz kaldı?
#
#  # her kategori için kaç TL harcadigimizi bulalım.
#  spent_by_category = shopping1.spent_by_category
#  assert isinstance(spent_by_category, dict)
#  # bu dict'in ilk elemani kategori adı (örneğin "gida"),
#  # ikinci elemani da o kategori için toplamda kaç TL harcadik, o olacak.
#  # dict'in ilk elemani, en yüksek harcama olsun, yani o kategorideki harcamaya göre
#  # büyükten kucuge sıralı olsun.
# for category in spent_by_category:
#      print(category, spent_by_category[category])


if __name__ == "__main__":
    main()
