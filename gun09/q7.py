# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
Q7 T.C. Kimlik Numarası Geçerli mi?
Verilen bir kimlik numarasının geçerli olup olmadığını True/False şeklinde döndüren bir fonksiyon yazınız.
https://seyler.eksisozluk.com/tc-kimlik-numaralarindaki-inanilmaz-algoritma
https://dinamiknetwork.com/tc-kimlik-no-dogrulama-algoritmasi/

"""


# 12345678901
# -----------
# 34297223248
# 3 2 7 2 2
# 22238526954


def dijit_mi(tc_kimlik_no):
    sonuc = False
    tc_kimlik = []
    for i in tc_kimlik_no:
        tc_kimlik.append(i);

    for j in tc_kimlik:
        if j.isdigit():
            sonuc += True
        else:
            sonuc = False

    return sonuc


def ilk_0_mu(tc_kimlik_no):
    pass


def haneler_arasi_iliski(tc_kimlik_no):
    # 1, 3, 5, 7 ve 9 hanesi toplamının 7 katından 2, 4, 6 ve 8 hanesi toplamı
    # çıkarıldığında sonucun 10'a bölünmesinden kalan sayı 10. basamaktaki sayı
    # ile aynı mı?
    tc_kimlik = []
    sonuc = False
    for i in tc_kimlik_no:
        tc_kimlik.append(i);

    if ((tc_kimlik[1] + tc_kimlik[3] + tc_kimlik[5] + tc_kimlik[7] + tc_kimlik[9])*7 - (tc_kimlik[2] + tc_kimlik[4] + tc_kimlik[6] + tc_kimlik[8]))%10 == tc_kimlik[10]:
        sonuc += True

    return sonuc


def tc_kimlik_no_dogrula(tc_kimlik_no):
    sonuc = False
    uzunluk = len(tc_kimlik_no)
    if dijit_mi(tc_kimlik_no):
        sonuc += True
    if ilk_0_mu(tc_kimlik_no):
        sonuc += True
    if haneler_arasi_iliski(tc_kimlik_no):
        sonuc += True


    while True:
        if uzunluk != 11:
            print("Lütfen 11 basamaklı rakamlar doldurunuz!")
            return sonuc
        else:
            print("buraya işlem gelecek..")
            # işlemler buraya gelecek..
        return sonuc


def main():
    tc_kimlik_no = input(">>>")
    tc_kimlik_no_dogrula(tc_kimlik_no)
    pass


if __name__ == "__main__":
    main()
