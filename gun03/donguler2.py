# utf-8
# @author: Zeki Gülen, 15/10/2020



# while dongusu

#

sayi = 0

while sayi<5:
    sayi = sayi + 1
    print(sayi)



deger = input("bir sayı giriniz..")
while True:
    if deger.

        # donguler2.py

        # break-continue

        kisi_bilgileri = ["tc12", "tc14", "tc25", "tc60"]
        # bu liste icinde her degerin tek oldugunu biliyoruz.

        aranan = "tc14"
        for kisi in kisi_bilgileri:
            print(kisi)
            if kisi == aranan:
                break  # donguyu kirar, donguden cikar.
        print("bitti")

        tum_filmler = ["game of thrones", "godzilla", "matrix", "batman", "lucy", "hababam sinifi", "amerikan pastasi"]
        asiri_siddetli_filmler = ["matrix"]

        aranan = "ma"
        for film in tum_filmler:
            if film in asiri_siddetli_filmler:
                continue
            if "ma" in film:
                print(film)

        for i in range(10):
            if i in [3, 7]:
                continue
            elif i == 8:
                break
            print(i)
        print("bitti")

        # while dongusu
        sayi = 1
        while sayi < 5:
            print(sayi)
            sayi = sayi + 1
            # sayi += 1

        print("_" * 40)

        # x = 1/2 + 2/3 + .... 10/11
        pay = 1
        toplam = 0
        while pay <= 10:
            payda = pay + 1
            terim = pay / payda
            toplam = toplam + terim
            print(pay, "/", payda)
            pay += 1
        print(toplam)  # 7.980122655122655

        toplam = 0
        pay = 1
        while True:
            payda = pay + 1
            terim = pay / payda
            toplam = toplam + terim
            pay = pay + 1
            if pay > 10:
                break
        print(toplam)

        for pay in range(1, 11):
            pass

        # input kisitlamak.
        # bir sayi giriniz.
        # while True:
        #     deger = input("bir sayi giriniz:")
        #     if deger.isdigit():
        #         break
        # print(deger)

        # kullanicidan, negatif bir sayi girilene kadar, sayi alip,
        # ortalamasini hesaplayan bir program yaziniz.
        # 10, 20, 30, -5 girerse, ortalamasi 20 olacak.

        # Alihan
        total = 0
        count = 0
        while True:
            num = input("Give a number: ").strip()
            if num[0] == "-" and num[1:].isdigit():
                break
            elif num.isdigit():
                num = int(num)
                total += num
                count += 1
            else:
                print("Invalid value")
                print()

        if count == 0:
            print("hic sayi girmediniz.")
        else:
            print(total / count)


