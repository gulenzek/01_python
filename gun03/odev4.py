# int değerler içeren bir listede en büyük 3 sayıyı bulma
# @author: Zeki Gülen, 16/10/2020

sayilar = []
toplam = 0
raw_sayilar = input(">>>")
r_s = ""

sayilar = raw_sayilar.split(",")

for raw_sayi in sayilar:
    r_s = raw_sayi.split()
    if sayi.isdigit():
        toplam = toplam + int(sayi)

print(toplam)