# lists1.py

# sequence: list, tuple
# sirali
# sorted, ordered

# list: ordered yani koydugumuz sirada bulunacaklar.
sayilar = [1, 3, 6, 8, 9]
print(type(sayilar))  # <class 'list'>

#          0  1  2  3  4
sayilar = [1, 2, 3, 4, "elma", "armut"]
sayilar = sayilar[:4]  # [1, 2, 3, 4]
print(sayilar)


# string'lere eleman eklemek.
film1 = "abc"
print(id(film1), "__1")  # 1875476792176
film1 = film1 + "d"
print(id(film1), "__2")  # 1875483911920

# listeye eleman eklemek.
# listeler: mutable
print(id(sayilar), "__3")  # 2113045717376
sayilar.append(7)
print(sayilar)
print(id(sayilar), "__4")  # 2113045717376

# [1, 2, 3, 4, 7]
sayilar[3] = 99
print(sayilar)
sayilar.append(10)
sayilar.append(23)

this_is_list = ["Labia Majora", "Labia Minora", "Clitoris", "Hymen", "Vagina", "Cervix"]

for elements in this_is_list:
    print(elements)

