# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
wrc1.py

en çok şampiyon olan 5 driver
en çok şampiyon olan 5 takim
peşpeşe en çok şampiyon olan pilot
peşpeşe en çok şampiyon olan takim
"""
import csv
import collections

def get_raw_data(dosya_adi) -> {}:
    with open(dosya_adi, "r", encoding="utf8") as csv_dosyasi:
        dosya_oku = csv.reader(csv_dosyasi, delimiter=";")
        sonuc = collections.deque()
        for satir in dosya_oku:
            sonuc.append(satir)
        sonuc.popleft()
        sonuc.popleft()

    return sonuc


def en_cok_sampiyon_olan_driver(datum, sampiyonluk=5):
    result = {}
    for data in datum:
        sampiyon = data[1]
        season = data[0]

    return result
    pass

def main():
    lines = get_raw_data("WRC.csv")
    en_cok_sampiyon_olan_driver(lines)

    # print(lines)
    # for line in lines:
    #     driver = {}
    #     line[1]
    #     # print(line[1])
    pass


if __name__ == "__main__":
    main()
