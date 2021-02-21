# Q1 sayı tahmin
# Bilgisayarın, 1'den 10'a kadar, random bir sayı tutmasini saglayin.
# Daha sonra kullanıcı, input() ile bu sayiyi tahmin etmesini isteyin.
# sonunda da, kaç seferde(kaç tahminde) bildiği bilgisini yazın.
# @author: Zeki Gülen, 15/10/2020

import random

sayi = random.randint(1, 10)
print(sayi)
sayac = 0
while True:
    tahmin = int(input("1-10 arası rakam >>>"))
    sayac = sayac + 1
    if sayi == 0:
        print("bilemediniz.. --", sayac)
        break
    elif tahmin > sayi:
        print("bilemediniz.. --", sayac)
        continue
    elif tahmin < sayi:
        print("bilemediniz.. --", sayac)
        continue
    else:
        break

print("tebrikler, {} sayısını {} defada tahmin ettiniz.".format(sayi, sayac))
