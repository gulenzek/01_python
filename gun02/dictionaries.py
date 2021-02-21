# dictionaries.py

# list, tuple, dictionary
# map.
# key->value
# anahtar->deger

engsozluk = {}
engsozluk["book"] = "kitap"
engsozluk["color"] = "renk"
engsozluk["python"] = "piton"
engsozluk["phone"] = "defter"  # bu degerin uzerine yazilacak.
engsozluk["phone"] = "telefon"

# daha once dict unordered bir tipti.
# python 3.6'dan sonra, ordered.

# bir elemana ulasmak, ekrana yazdirmak.
print(engsozluk["color"])

# in (membership, uyelik) operatoru
# print(engsozluk["mouse"])
# KeyError: 'mouse'

if "mouse" in engsozluk:
    print(engsozluk["mouse"])

deger1 = engsozluk.get("mouse", None)
deger2 = engsozluk.get("book", None)

tum_degerler = engsozluk.items()


# uygulama: şifre kontrolu
# + kullanıcının sifrelerinin olduğu bir dict olsun.
# + kullanıcıdan, kullanıcı adı ve şifre alalım.
# login olabiliyorsa, login oldun diyelim.
# degilse, olmadığını belirtelim.
sifreler = {}
sifreler["darkL0rd122"] = "123"
sifreler["caglar"] = "abc"
sifreler["serdar"] = "456"

username = "serdar"
password = "456"

# None yazmazsak, default None dondurur:
password2 = sifreler.get(username)
if password == password2:
    print("login oldunuz")
else:
    print("login olamadiniz.")


# hangi tipler key olabilir?
d1 = {}
d1[3] = "uc"
# int olur, float olur, string olur.

ucuslar = {}
# TypeError: unhashable type: 'list'
# hash?
# MD5, clash

ucus_bilgileri1 = ("caglar" ,"tc110", "pnr95")
ucus_bilgileri2 = ("serdar" ,"tc115", "pnr95")
ucuslar[ucus_bilgileri1] = "27A"
ucuslar[ucus_bilgileri2] = "28B"

# ucus_bilgileri2[0] = "caglar"
# ucus_bilgileri2[1] = "tc110"
# list: mutable
# tuple


# il-dictionary ornegi
# kullanıcıdan bir il bilgisi alalım.
# değeri ekrana yazalım.
# bilmediğimiz bir il ise, plaka kodu ve bölgesini soralım.
# iller içine ekleyelim.
iller = {}
iller["adana"] = ("01", "akdeniz")
iller["ordu"] = ("52", "karadeniz")
iller["samsun"] = ("55", "karadeniz")
iller["izmir"] = ("35", "ege")
iller["erzurum"] = ("25", "doğu anadolu")
iller["istanbul"] = ("34", "marmara")
# kastamonu, 37
sorgulanan_il_adi = "samsun"
il_bilgisi = iller.get(sorgulanan_il_adi)
if il_bilgisi:
    print(il_bilgisi)
else:
    plaka = input("plakayi_giriniz:")
    bolge = input("bolgeyi giriniz:")
    iller[sorgulanan_il_adi] = (plaka, bolge)
    print(iller)


keys = iller.keys()

values = iller.values()

print(len(iller), "__1")
del iller["samsun"]
print(len(iller), "__2")

print(len(iller), "__3")
silinen_eleman = iller.pop("ordu")
iller.pop("izmir")  # bu da ok.
print(len(iller), "__4")
print(silinen_eleman)

print("done")

# -----------------------------------------------------------

# dictionaries.py

# list, tuple, dictionary
# map.
# key->value
# anahtar->deger

engsozluk = {}
engsozluk["book"] = "kitap"
engsozluk["color"] = "renk"
engsozluk["python"] = "piton"
engsozluk["phone"] = "defter"  # bu degerin uzerine yazilacak.
engsozluk["phone"] = "telefon"

# daha once dict unordered bir tipti.
# python 3.6'dan sonra, ordered.

# bir elemana ulasmak, ekrana yazdirmak.
print(engsozluk["color"])

# in (membership, uyelik) operatoru
# print(engsozluk["mouse"])
# KeyError: 'mouse'

if "mouse" in engsozluk:
    print(engsozluk["mouse"])

deger1 = engsozluk.get("mouse", None)
deger2 = engsozluk.get("book", None)

tum_degerler = engsozluk.items()


# uygulama: şifre kontrolu
# + kullanıcının sifrelerinin olduğu bir dict olsun.
# + kullanıcıdan, kullanıcı adı ve şifre alalım.
# login olabiliyorsa, login oldun diyelim.
# degilse, olmadığını belirtelim.
sifreler = {}
sifreler["darkL0rd122"] = "123"
sifreler["caglar"] = "abc"
sifreler["serdar"] = "456"

username = "serdar"
password = "456"

# None yazmazsak, default None dondurur:
password2 = sifreler.get(username)
if password == password2:
    print("login oldunuz")
else:
    print("login olamadiniz.")


# hangi tipler key olabilir?
d1 = {}
d1[3] = "uc"
# int olur, float olur, string olur.

ucuslar = {}
# TypeError: unhashable type: 'list'
# hash?
# MD5, clash

ucus_bilgileri1 = ("caglar" ,"tc110", "pnr95")
ucus_bilgileri2 = ("serdar" ,"tc115", "pnr95")
ucuslar[ucus_bilgileri1] = "27A"
ucuslar[ucus_bilgileri2] = "28B"

# ucus_bilgileri2[0] = "caglar"
# ucus_bilgileri2[1] = "tc110"
# list: mutable
# tuple


# il-dictionary ornegi
# kullanıcıdan bir il bilgisi alalım.
# değeri ekrana yazalım.
# bilmediğimiz bir il ise, plaka kodu ve bölgesini soralım.
# iller içine ekleyelim.
iller = {}
iller["adana"] = ("01", "akdeniz")
iller["ordu"] = ("52", "karadeniz")
iller["samsun"] = ("55", "karadeniz")
iller["izmir"] = ("35", "ege")
iller["erzurum"] = ("25", "doğu anadolu")
iller["istanbul"] = ("34", "marmara")
# kastamonu, 37
sorgulanan_il_adi = "samsun"
il_bilgisi = iller.get(sorgulanan_il_adi)
if il_bilgisi:
    print(il_bilgisi)
else:
    plaka = input("plakayi_giriniz:")
    bolge = input("bolgeyi giriniz:")
    iller[sorgulanan_il_adi] = (plaka, bolge)
    print(iller)


keys = iller.keys()

values = iller.values()

print(len(iller), "__1")
del iller["samsun"]
print(len(iller), "__2")

print(len(iller), "__3")
silinen_eleman = iller.pop("ordu")
iller.pop("izmir")  # bu da ok.
print(len(iller), "__4")
print(silinen_eleman)

print("done")


