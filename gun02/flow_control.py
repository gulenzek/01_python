# flow_control.py


izlendi : bool
izlendi = False

if izlendi:
    print("Valuesu yok")
pass


# dangling else problem

# "Kontrol + Shift + A" önemli...

puan = 52

puan_tahmini = int(input("Giriniz:"))
if puan_tahmini>=86 and puan_tahmini<=100:
    print("A")
elif puan_tahmini>=66 and puan_tahmini<=85:
    print("B")
elif puan_tahmini>=51 and puan_tahmini<=65:
    print("C")
elif puan_tahmini<=50:
    print("D")

# flow_control.py
# akış denetimi

# statement
# branching, decision making, flow control, akış denetimi
# loops, döngüler

# boolean
# George Bool

izlendi = True
izlendi = False

kedi_mi = True
yaramaz_mi = False

yaramazlik_yapar_mi = kedi_mi and yaramaz_mi

# and
# or
# not

print(True and True)  # True
print(True and False)  # F
print(False and True)  # F
print(False and False)  # F

print("or" * 30)

print(True or True)  # True
print(True or False)  # T
print(False or True)  # T
print(False or False)  # F

# negate
print(not True)  # F
print(not False)  # T


# karsilastirma operatorleri
# ==, !=, <, >, <=, >=

# atama operatorleri
# =
a = 5
# +=, -=
a = a + 2
a += 2  # ustteki ile ayni.s

# bunlar da var, ama daha az kullaniliyor:
# /=, *=, //=, **=


# if deyimi
print("_if" * 30)
dolu_yagacak_mi = True
if dolu_yagacak_mi:
    print("dolu yagacak")
    print("araban varsa, battaniye bul")
# elif dolu_yagacak_mi == False:
else:
    print("gonul rahatligiyla uyuyabilirsin.")

# dolu yagmis olsa da, olmasa da:
print("gunaydin")


kedi_yaramaz_mi = True
if kedi_yaramaz_mi == False:
    print("sana kolay gelsin")
else:
    pass

# ic ice 2 if
dolu_yagacak_mi = True
araban_var_mi = False
if dolu_yagacak_mi:
    print("dolu yagacak")
    if araban_var_mi:
        print("battaniye bul")
    else:
        print("kafani korusan yeter.")
# elif dolu_yagacak_mi == False:
else:
    print("gonul rahatligiyla uyuyabilirsin.")


# if-elif-elif-elif-else
# cekilis
bizim_sayi = 7  # bilet, tahmin ettigimiz sayi

# 9 kazaniyor.
# +-2 9 amorti kazansin.
# diger sayilar hic kazanamadi

if bizim_sayi == 9:
    print("kazandiniz")
elif abs(bizim_sayi-9) <= 2:
    print("amorti kazandiniz.")
elif bizim_sayi == 100:
    print("tanidik kontenjanindan kazandiniz.")
else:
    print("hic kazanamadiniz.")
# if: 1 tane yazmak zorundayim.
# pek cok elif yazabilirim. (ya da 0)
# elif: else+if
# else, yazarsam, 1 tane yazabilirim.



# not ortalamasi hesaplama uygulamasi.
# D: 0 .. 50
# C: 51 .. 65
# B: 66 .. 85
# A: 86 .. +

puan = 52
harf = None
if 0<=puan and puan<=50:
    harf = "D"
elif 51<=puan<=65:
    harf = "C"
elif 66<=puan<=85:
    harf = "B"
elif 86<=puan:
    harf = "A"
else:
    harf = None
print(harf)

# D: 0 .. 50
# C: 51 .. 65
# B: 66 .. 85
# A: 86 .. +
if puan >= 86:
    harf = "A"
elif puan >= 66:
    harf = "B"
elif puan >= 51:
    harf = "C"
elif puan >= 0:
    harf = "D"
else:
    harf = None

# yanlis olacakti:
# if puan >= 0:
#     harf = "D"
# elif puan >= 51:
#     harf = "C"
# ....


print("done")


# ------------------------------------------------------

# flow_control.py
# akış denetimi

# statement
# branching, decision making, flow control, akış denetimi
# loops, döngüler

# boolean
# George Bool

izlendi = True
izlendi = False

kedi_mi = True
yaramaz_mi = False

yaramazlik_yapar_mi = kedi_mi and yaramaz_mi

# and
# or
# not

print(True and True)  # True
print(True and False)  # F
print(False and True)  # F
print(False and False)  # F

print("or" * 30)

print(True or True)  # True
print(True or False)  # T
print(False or True)  # T
print(False or False)  # F

# negate
print(not True)  # F
print(not False)  # T


# karsilastirma operatorleri
# ==, !=, <, >, <=, >=

# atama operatorleri
# =
a = 5
# +=, -=
a = a + 2
a += 2  # ustteki ile ayni.s

# bunlar da var, ama daha az kullaniliyor:
# /=, *=, //=, **=


# if deyimi
print("_if" * 30)
dolu_yagacak_mi = True
if dolu_yagacak_mi:
    print("dolu yagacak")
    print("araban varsa, battaniye bul")
# elif dolu_yagacak_mi == False:
else:
    print("gonul rahatligiyla uyuyabilirsin.")

# dolu yagmis olsa da, olmasa da:
print("gunaydin")


kedi_yaramaz_mi = True
if kedi_yaramaz_mi == False:
    print("sana kolay gelsin")
else:
    pass

# ic ice 2 if
dolu_yagacak_mi = True
araban_var_mi = False
if dolu_yagacak_mi:
    print("dolu yagacak")
    if araban_var_mi:
        print("battaniye bul")
    else:
        print("kafani korusan yeter.")
# elif dolu_yagacak_mi == False:
else:
    print("gonul rahatligiyla uyuyabilirsin.")


# if-elif-elif-elif-else
# cekilis
bizim_sayi = 7  # bilet, tahmin ettigimiz sayi

# 9 kazaniyor.
# +-2 9 amorti kazansin.
# diger sayilar hic kazanamadi

if bizim_sayi == 9:
    print("kazandiniz")
elif abs(bizim_sayi - 9) <= 2:
    print("amorti kazandiniz.")
elif bizim_sayi == 100:
    print("tanidik kontenjanindan kazandiniz.")
else:
    print("hic kazanamadiniz.")
# if: 1 tane yazmak zorundayim.
# pek cok elif yazabilirim. (ya da 0)
# elif: else+if
# else, yazarsam, 1 tane yazabilirim.



# not ortalamasi hesaplama uygulamasi.
# D: 0 .. 50
# C: 51 .. 65
# B: 66 .. 85
# A: 86 .. +

puan = 52
harf = None
if 0<=puan and puan<=50:
    harf = "D"
elif 51<=puan<=65:
    harf = "C"
elif 66<=puan<=85:
    harf = "B"
elif 86<=puan:
    harf = "A"
else:
    harf = None
print(harf)

# D: 0 .. 50
# C: 51 .. 65
# B: 66 .. 85
# A: 86 .. +
if puan >= 86:
    harf = "A"
elif puan >= 66:
    harf = "B"
elif puan >= 51:
    harf = "C"
elif puan >= 0:
    harf = "D"
else:
    harf = None

# yanlis olacakti:
# if puan >= 0:
#     harf = "D"
# elif puan >= 51:
#     harf = "C"
# ....


print("operator ve 2 sayi almak" + "_" * 30)
# kullanicidan 2 sayi ve bir de operator alacagiz.
# buna gore bir islemi yapip, sonucunu bildirelim.
ifade = "45/9"  # str
# operand, operator, operand
# parcalar = ifade.split("+")
operator = None
if "+" in ifade:
    operator = "+"
elif "-" in ifade:
    operator = "-"
elif "*" in ifade:
    operator = "*"
elif "/" in ifade:
    operator = "/"
# bu satira geldgimizde,
# operator None ise, demek ki giris hatali.

# # alternatif, dogru:
# if operator is None:
#     print("hatali giris")
# else:
#     operands = ifade.split(operator)
#
# # alternatif, dogru:
# if operator is not None:
#     operands = ifade.split(operator)
# else:
#     print("hatali giris")

sonuc = None
if operator:
    operands = ifade.split(operator)
    number1 = None
    number2 = None
    if operands[0].isdigit():
        number1 = float(operands[0])
    if operands[1].isdigit():
        number2 = float(operands[1])

    if number1 is not None and number2 is not None:
        # bu noktada, elimde 2 float sayi ve str operator var.
        if operator == "+":
            sonuc = number1 + number2
        elif operator == "-":
            sonuc = number1 - number2
        elif operator == "*":
            sonuc = number1 * number2
        elif operator == "/":
            if number2 == 0:
                print("0'a bolemeyiz.")
                sonuc = None
            else:
                sonuc = number1 / number2
else:
    print("hatali giris")
print("sonuc", sonuc)

print("done")


# flow_control.py
# akış denetimi

# statement
# branching, decision making, flow control, akış denetimi
# loops, döngüler

# boolean
# George Bool

izlendi = True
izlendi = False

kedi_mi = True
yaramaz_mi = False

yaramazlik_yapar_mi = kedi_mi and yaramaz_mi

# and
# or
# not

print(True and True)  # True
print(True and False)  # F
print(False and True)  # F
print(False and False)  # F

print("or" * 30)

print(True or True)  # True
print(True or False)  # T
print(False or True)  # T
print(False or False)  # F

# negate
print(not True)  # F
print(not False)  # T


# karsilastirma operatorleri
# ==, !=, <, >, <=, >=

# atama operatorleri
# =
a = 5
# +=, -=
a = a + 2
a += 2  # ustteki ile ayni.s

# bunlar da var, ama daha az kullaniliyor:
# /=, *=, //=, **=


# if deyimi
print("_if" * 30)
dolu_yagacak_mi = True
if dolu_yagacak_mi:
    print("dolu yagacak")
    print("araban varsa, battaniye bul")
# elif dolu_yagacak_mi == False:
else:
    print("gonul rahatligiyla uyuyabilirsin.")

# dolu yagmis olsa da, olmasa da:
print("gunaydin")


kedi_yaramaz_mi = True
if kedi_yaramaz_mi == False:
    print("sana kolay gelsin")
else:
    pass

# ic ice 2 if
dolu_yagacak_mi = True
araban_var_mi = False
if dolu_yagacak_mi:
    print("dolu yagacak")
    if araban_var_mi:
        print("battaniye bul")
    else:
        print("kafani korusan yeter.")
# elif dolu_yagacak_mi == False:
else:
    print("gonul rahatligiyla uyuyabilirsin.")


# if-elif-elif-elif-else
# cekilis
bizim_sayi = 7  # bilet, tahmin ettigimiz sayi

# 9 kazaniyor.
# +-2 9 amorti kazansin.
# diger sayilar hic kazanamadi

if bizim_sayi == 9:
    print("kazandiniz")
elif abs(bizim_sayi - 9) <= 2:
    print("amorti kazandiniz.")
elif bizim_sayi == 100:
    print("tanidik kontenjanindan kazandiniz.")
else:
    print("hic kazanamadiniz.")
# if: 1 tane yazmak zorundayim.
# pek cok elif yazabilirim. (ya da 0)
# elif: else+if
# else, yazarsam, 1 tane yazabilirim.



# not ortalamasi hesaplama uygulamasi.
# D: 0 .. 50
# C: 51 .. 65
# B: 66 .. 85
# A: 86 .. +

puan = 52
harf = None
if 0<=puan and puan<=50:
    harf = "D"
elif 51<=puan<=65:
    harf = "C"
elif 66<=puan<=85:
    harf = "B"
elif 86<=puan:
    harf = "A"
else:
    harf = None
print(harf)

# D: 0 .. 50
# C: 51 .. 65
# B: 66 .. 85
# A: 86 .. +
if puan >= 86:
    harf = "A"
elif puan >= 66:
    harf = "B"
elif puan >= 51:
    harf = "C"
elif puan >= 0:
    harf = "D"
else:
    harf = None

# yanlis olacakti:
# if puan >= 0:
#     harf = "D"
# elif puan >= 51:
#     harf = "C"
# ....


print("operator ve 2 sayi almak" + "_" * 30)
# kullanicidan 2 sayi ve bir de operator alacagiz.
# buna gore bir islemi yapip, sonucunu bildirelim.
ifade = "45/9"  # str
# operand, operator, operand
# parcalar = ifade.split("+")
operator = None
if "+" in ifade:
    operator = "+"
elif "-" in ifade:
    operator = "-"
elif "*" in ifade:
    operator = "*"
elif "/" in ifade:
    operator = "/"
# bu satira geldgimizde,
# operator None ise, demek ki giris hatali.

# # alternatif, dogru:
# if operator is None:
#     print("hatali giris")
# else:
#     operands = ifade.split(operator)
#
# # alternatif, dogru:
# if operator is not None:
#     operands = ifade.split(operator)
# else:
#     print("hatali giris")

sonuc = None
if operator:
    operands = ifade.split(operator)
    number1 = None
    number2 = None
    if operands[0].isdigit():
        number1 = float(operands[0])
    if operands[1].isdigit():
        number2 = float(operands[1])

    if number1 is not None and number2 is not None:
        # bu noktada, elimde 2 float sayi ve str operator var.
        if operator == "+":
            sonuc = number1 + number2
        elif operator == "-":
            sonuc = number1 - number2
        elif operator == "*":
            sonuc = number1 * number2
        elif operator == "/":
            if number2 == 0:
                print("0'a bolemeyiz.")
                sonuc = None
            else:
                sonuc = number1 / number2
else:
    print("hatali giris")
print("sonuc", sonuc)

print("done")


