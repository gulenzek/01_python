# fonksiyonlar python -- değer döndürmezse None oluyor..

def f(x: int) -> int:
    sonuc = 3 * x + 4
    return sonuc


sonuc1 = f(4)
sonuc2 = f(2)

print(sonuc1)
print(sonuc2)



# functions1.py

s1 = ""
s1.split(",")
s1.split("_")


x = print("abc")
print(x, "xx")  # None

# f(x) = 3x + 4

def f(x):
    sonuc = 3 * x + 4
    return sonuc


sonuc2 = f(2)
print(sonuc2)  # None, 10

print("def")

def bolenleri_getir(sayi):
    tam_bolenler = []
    for i in range(1, sayi // 2 + 1):
        if sayi % i == 0:
            tam_bolenler.append(i)
    tam_bolenler.append(sayi)  # kendisini ekler
    return tam_bolenler
