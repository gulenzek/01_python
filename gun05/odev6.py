# Q6
# verilen bir sayidan büyük bir sonraki asal sayiyi bulan uygulama.

sayi = 100
sayac = 0
for i in range(3, sayi):
    for j in range(3,i):
        if i%j==0:
            sayac += 1
    if sayac == 0:
        print("asal.")

def is_prime(sayi):
    sonuc = False

    return sonuc
