def bolenleri_getir(sayi):
    tam_bolenler = []
    for i in range(1, sayi // 2 + 1):
        if sayi % i == 0:
            tam_bolenler.append(i)
    tam_bolenler.append(sayi)  # kendisini ekler
    return tam_bolenler

print(bolenleri_getir(100))