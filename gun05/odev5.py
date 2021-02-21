# Q5
# verilen bir sayıya kadar olan asal sayıları bulan uygulama
# .yukarıdaki is_prime() fonksiyonunu tekrar kullanabilirsiniz.
import time


def asal(asal_sayi_mi: int):
    """Asal sayı bulan fonksiyon
    Girdi olarak bir sayı alır
    Bu sayıya kadar olan asal sayıları ekrana basar.
    """
    sayac = 0
    for sayi in range(2, asal_sayi_mi):
        sayac = 0
        for bolen in range(2, sayi):
            if (sayi % bolen == 0):
                sayac += 1
        if sayac == 0:
            print(sayi, "bir asal sayıdır.")
            pass
    return


t1 = time.time()
print(asal(200))
t2 = time.time()

print(t2-t1)

