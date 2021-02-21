# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
- [ ] En çok gol atan takım
- [ ] En az gol yiyen takım
- [ ] En farklı skorla biten 10 maç
- [ ] En çok gol atılan 10 maç
- [ ] En çok maç oynanmış şehir
- [ ] En çok maç oynanmış ülke
- [ ] En Uzun Yenilmezlik ünvanı
- [ ] Her bir turnuvadaki mac sayısı
"""
import csv, datetime


def get_raw_data(dosya_adi) -> {}:
    with open(dosya_adi, "r", encoding="utf8") as csv_dosyasi:
        dosya_oku = csv.reader(csv_dosyasi, delimiter=",")
        sonuc = []
        for satir in dosya_oku:
            datum = {}
            if satir[0] == "date":
                continue
            datum["Date"] = satir[0]
            datum["Sehir Ulke"] = satir[1]
            datum["Home Team"] = satir[2]
            datum["Away Team"] = satir[3]
            datum["Home Goals"] = int(satir[4])
            datum["Away Goals"] = int(satir[5])
            sonuc.append(datum)
        sonuc.pop(0)
    return sonuc


def en_cok_gol_atan_takim(datum):
    result = {}
    for data in datum:
        home_goal = data["Home Goals"]
        away_goal = data["Away Goals"]
        result[data["Home Team"]] = result.get(data["Home Team"], 0) + home_goal
        result[data["Away Team"]] = result.get(data["Away Team"], 0) + away_goal

    team_name, team_goals = max(result.items(), key=lambda item: item[1])

    return team_name, team_goals


def en_az_gol_yiyen_takim(datum):
    result = {}
    for data in datum:
        home_yedigi_gol = data["Away Goals"]
        away_yedigi_gol = data["Home Goals"]
        result[data["Home Team"]] = result.get(data["Home Team"], 0) + home_yedigi_gol
        result[data["Away Team"]] = result.get(data["Away Team"], 0) + away_yedigi_gol

    team_name, team_goals = min(result.items(), key=lambda item: item[1])

    return team_name, team_goals


def en_farkli_skorla_biten_mac(datum):
    dd = datum[::]
    result = sorted(dd, key=lambda item: abs(item["Home Goals"] - item["Away Goals"]), reverse=True)

    return result


def en_farkli_skorla_biten_mac(datum):
    dd = datum[::]
    result = sorted(dd, key=lambda item: abs(item["Home Goals"] + item["Away Goals"]), reverse=True)

    return result[:10]


def en_cok_mac_oynanmis_sehir(datum):
    dd = datum[::]
    result = sorted(dd, key=lambda item: abs(item["Home Goals"] + item["Away Goals"]), reverse=True)

    return result[:10]


my_data = get_raw_data("results.csv")
en_cok_gol_atan_takim(my_data)
en_az_gol_yiyen_takim(my_data)
result = en_farkli_skorla_biten_mac(my_data)
print("done")

#
# def main():
#     dosya_adi = "results.csv"
#     data = {}
#     data = get_raw_data(dosya_adi)
#     en_cok_gol_atan_takim = {}
#     en_az_gol_yiyen_takim = {}
#     en_farkli_skorla_biten_mac = {}
#     en_cok_gol_atilan_10_mac = {}
#     en_cok_mac_oynanmis_sehir = {}
#     en_cok_mac_oynanmis_ulke = {}
#     en_uzun_yenilmezlik_unvani = {}
#     her_bir_turnuvadaki_mac_sayisi = {}
#     print(len(data))
#     sehir = []
#     for satir in data:
#         parcalar = str(satir[1]).strip().split(",")
#         # en_cok_gol_atan_takim[]
#         sehir.append(parcalar[0])
#     print(sehir)
#     # sehir listemiz var.
#     sehirim = []
#     for line in sehir:
#         sehirim.append(str(line).strip().split(","))
#     print(sehirim)
#
#     gol_sayisi1 = 0
#     gol_sayisi2 = 0
#     for satir in data:
#         gol_sayisi1 += int(satir[4])
#         gol_sayisi2 += int(satir[5])
#
#     print(gol_sayisi1, gol_sayisi2)
#     pass
#
#
# if __name__ == "__main__":
#     main()
