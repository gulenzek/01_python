# Odanın en, boy, yüksekliklerini soran ve hacmini hesaplayan bir program.
# Zeki Gülen, 14/10/2020

en = float(input("Odanın eni kaç metre? :"))
boy = float(input("Odanın boyu kaç metre? :"))
yukseklik = float(input("Odanın yüksekliği kaç metre? :"))

hacim= en*boy*yukseklik
print("Odanın hacmi ", str(hacim), "metreküptür.")


# Bahşiş hesabı
# Zeki Gülen, 14/10/2020

siparis = float(input("Sipariş tutarı ne kadar?"))
bahsis_oranı = int(input("5%, 10%, 15%? :"))
bahsis = (bahsis_oranı*siparis)/100
print("Sipariş: ", siparis)
print("Bahşiş: ", bahsis)
print("Toplam tutar: ", siparis + bahsis, " TL'dir.")

# İlk n pozitif sayının toplamı

n = int(input("Toplanacak rakam kaçtır? :"))
toplam = (n*(n+1))/2
print("Toplam: ", toplam)

for i in n:
    toplam += i
    print(toplam)
