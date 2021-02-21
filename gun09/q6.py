# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
Satranç tahtası yerleşimi aşağıdaki gibidir. Bunu referans alarak, kullanıcıdan
bir koordinat alarak (örneğin d4), bunun siyah mı yoksa beyaz mı olduğunu
döndüren bir fonksiyon yazınız.
"""


def satranc_tahtasi():
    satranc = []
    for i in range(1, 9, 1):
        for j in range(1, 9, 1):
            if (i + j) % 2 == 0:
                satranc.append([[i, j], "Siyah"])
            else:
                satranc.append([[i, j], "Beyaz"])
    return satranc


def renk_soyle(koordinat_giris):
    harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rakamlar = [1, 2, 3, 4, 5, 6, 7, 8]
    sonuc = ['Siyah', 'Beyaz']

    while True:
        if koordinat_giris[0] in harfler:
            print(koordinat_giris[0])
            if koordinat_giris[1] in rakamlar:
                print("fonksiyon çağır..")
            else:
                print(koordinat_giris[1])
                print("lütfen tekrar deneyiniz..")
                break

    return sonuc


def main():
    print(satranc_tahtasi())
    print(renk_soyle('a5'))
    pass


if __name__ == "__main__":
    main()
