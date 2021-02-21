# Faktöriyel hesabı
# @Zeki Gülen, 15/10/2020
sayi = int(input(">>>"))
toplam = 1
for n in range(sayi):
    toplam += toplam*(n)
print(toplam)