def cift_sayilarin_toplami(n):
	toplam = 0
	n = n+1
	for sayi in range(n):
		if sayi % 2 == 0:
			toplam += sayi
	return toplam
print(cift_sayilarin_toplami(10))