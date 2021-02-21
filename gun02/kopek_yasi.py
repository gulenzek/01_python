# -*- coding: utf-8 -*-
# Bir yaklaşıma göre, bir insan yılının, 7 köpek yılına eşit olduğu söylenir.
# Yani, 1 yaşındaki bir köpek, 7 yaşındaki bir insana eşit yaşta gibi düşünü-
# lebilir. Ama, toplam yaşam süresi, ve köpeklerin 2 yılda yetişkin hale gel-
# diği düşünülürse, bu yaklaşım doğru değildir.
#
# İkinci bir yaklaşım, köpeklerin ilk 2 yılını 10.5 yıl sayıp, daha sonraki
# yıllarını da 4 yıl olarak saymayı önerir. Bu ikinci yaklaşıma göre, bir in-
# sanın yaşını alıp, köpek olarak kaç yaşında olacağını hesaplayan bir program
# yazınız.
# @author: Zeki Gülen, Created on Thu Oct 15 09:26:40 2020

yas = int(input("Yaşınız? :"))
print("1. yaklaşım --> Yaşınız", yas, "sizinle birlikte doğan köpek", yas*7, "köpek yaşında.")

if yas > 2:
    kopek_yasi = 10.5 + ((yas-2)/4)
else:
    kopek_yasi = yas*10.5/2
print("2. yaklaşım --> Yaşınız", yas, "sizinle birlikte doğan köpek", kopek_yasi, "köpek yaşında.")




