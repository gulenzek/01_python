# Q2 - Kullanıcıdan "a,b,c,d", "4,8,2,4" şeklinde verileri alıp toplayan program.
# @author: Zeki Gülen, 16/10/2020

toplanacak_ifade = input(">>>")
toplam = 0
for sayi in toplanacak_ifade:
    if sayi.isdigit():
        toplam = toplam + int(sayi)
print("Toplam {}.".format(toplam))
# while True:
# if toplanacak_deger