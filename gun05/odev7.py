# Q7 zaman hesapla
# •	t = x/v formülünü kullanalım.
# •	iki parametre döndürsün: saat ve dakika
# def zaman_hesapla(ortalama_hiz, mesafe):
#     """
#     Ortalama hiz ve mesafe kullanarak sureyi hesaplar.
#
#     bu fonksiyon soyle cagirilir:
#     saat, dakika = zaman_hesapla(ortalama_hiz, mesafe)
#
#     :param ortalama_hiz:
#     :param mesafe:
#     :return:
#     """
#     pass
import time
v_ = 30 # km/saat
mesafe = 120 # km


def zaman_hesapla(v_km_bolu_saat, mesafe_km):
    zaman = 0
    zaman = mesafe_km / v_km_bolu_saat
    saat = int(str(zaman).split('.')[0])
    dakika = round(float("0." + str(str(zaman).split('.')[1]))*60)
    return saat, dakika

print(zaman_hesapla(90, 950)[0], "saat, ", zaman_hesapla(90, 950)[1], "dakika")
print(zaman_hesapla(3, 20))