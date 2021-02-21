# for, while

# iterable
sehirler = ["istanbul", "izmir", "ankara"]
for sehir in sehirler:
    pass
    # print(sehir)

for item in sehirler:
    pass

iller = {}
iller["adana"] = ("01", "akdeniz")
iller["ordu"] = ("52", "karadeniz")
iller["samsun"] = ("55", "karadeniz")
iller["izmir"] = ("35", "ege")
iller["erzurum"] = ("25", "doğu anadolu")
iller["istanbul"] = ("34", "marmara")
# karadeniz bolgesindeki illeri(il adi, plaka) yazmak

for il in iller:
    # dict uzerinde uygularsak, bize her seferinde key getirir.
    il_bilgisi = iller[il]
    plaka = il_bilgisi[0]
    bolge = il_bilgisi[1]
    if bolge == "karadeniz":
        print(il, plaka, bolge)
    # print(il, il_bilgisi)

# x, y = 3, 5, 6
# (<class 'ValueError'>, ValueError('too many values to unpack (expected 2)'), <traceback object at 0x0000022C95631B80>)

# x, y, z = 3, 5
# (<class 'ValueError'>, ValueError('not enough values to unpack (expected 3, got 2)'), <traceback object at 0x000001994A42A680>)

x = 3, 5  # tuple
x, y = 3, 4

print(iller.items())
for il, il_bilgisi in iller.items():
    print(il, il_bilgisi)


tum_filmler = ["game of thrones", "godzilla", "matrix", "batman", "lucy", "hababam sinifi", "amerikan pastasi"]
# icinde "ma" gecen filmleri bir listede toplayalim.
aranan = "ma"
bulunanlar = []
for film in tum_filmler:
    # bir filmin icinde ma gecip gecmedigini nasil bulurum?
    if film.find(aranan) != -1:
        bulunanlar.append(film)
    if aranan in film:
        pass

print("done")


# ------------------------------------------------------

# for, while

# iterable
sehirler = ["istanbul", "izmir", "ankara"]
for sehir in sehirler:
    pass
    # print(sehir)

for item in sehirler:
    pass

iller = {}
iller["adana"] = ("01", "akdeniz")
iller["ordu"] = ("52", "karadeniz")
iller["samsun"] = ("55", "karadeniz")
iller["izmir"] = ("35", "ege")
iller["erzurum"] = ("25", "doğu anadolu")
iller["istanbul"] = ("34", "marmara")
# karadeniz bolgesindeki illeri(il adi, plaka) yazmak

for il in iller:
    # dict uzerinde uygularsak, bize her seferinde key getirir.
    il_bilgisi = iller[il]
    plaka = il_bilgisi[0]
    bolge = il_bilgisi[1]
    if bolge == "karadeniz":
        print(il, plaka, bolge)
    # print(il, il_bilgisi)

# x, y = 3, 5, 6
# (<class 'ValueError'>, ValueError('too many values to unpack (expected 2)'), <traceback object at 0x0000022C95631B80>)

# x, y, z = 3, 5
# (<class 'ValueError'>, ValueError('not enough values to unpack (expected 3, got 2)'), <traceback object at 0x000001994A42A680>)

x = 3, 5  # tuple
x, y = 3, 4

print(iller.items())
for il, il_bilgisi in iller.items():
    print(il, il_bilgisi)


tum_filmler = ["game of thrones", "godzilla", "matrix", "batman", "lucy", "hababam sinifi", "amerikan pastasi"]
# icinde "ma" gecen filmleri bir listede toplayalim.
aranan = "ma"
bulunanlar = []
for film in tum_filmler:
    # bir filmin icinde ma gecip gecmedigini nasil bulurum?
    if film.find(aranan) != -1:
        bulunanlar.append(film)
    if aranan in film:
        pass


# tuple, ayni list gibi donuluyor.

# string uzerinde dongu
film_adi = "batman"
for harf in film_adi:
    print(harf)

# range()
for n in range(5):  # 0..5 dahil degil.
    print(n)

for n in range(3, 9):
    # start, stop(dahil degil)
    print(n)

for n in range(3, 9, 2):
    # start, stop(dahil degil), step
    print(n)


# x = 1/2 + 2/3 + 3/4 + ..... 10/11
# x'in degerini hesaplayiniz.
toplam = 0
for pay in range(1, 11):
    payda = pay + 1
    terim = pay/(pay+1)
    toplam += terim
print(toplam)
# 7.980122655122655

data = [[3, 9, 4], [5, 2, 9], [8, 2, 5]]
# bu listedeki tum elemanlarin toplami nedir?




print("done")
