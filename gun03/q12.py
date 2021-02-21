def count_chars(str1) -> dict:
    karakter_sayilari = {}
    for karakter in str1:  # stringin karakter olarak ayrışmasını sağlıyoruz..
        keys = karakter_sayilari.keys()
        if karakter in keys:
            karakter_sayilari[karakter] += 1
        else:
            karakter_sayilari[karakter] = 1
    return karakter_sayilari


print(count_chars('merhaba merhaba'))

from bs4 import pip