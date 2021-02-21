# Q3 - Kullanıcıdan bir n sayısı alıp n+nn+nnn hesabı yapan program.
# @author: Zeki Gülen, 16/10/2020

sayi = input(">>>")
toplam = 0
if sayi.isdigit():
    toplam = int(sayi) + int(str(sayi) + str(sayi)) + int(str(sayi) + str(sayi) + str(sayi))

print("n + nn + nnn = ", str(toplam))