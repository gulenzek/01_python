# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""
import nltk

harita = {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', 'f':'', 'g':'', 'h':'', 'i':'', 'j':'',
               'k':'', 'l':'', 'm':'', 'n':'', 'o':'', 'p':'', 'q':'', 'r':'', 's':'', 't':'',
               'u':'', 'v':'', 'w':'', 'x':'', 'y':'', 'z':''}

raw_text = open("musvedde.txt", "r", encoding="utf8")
metin = raw_text.read()
print(metin)
butun_sozcukler = nltk.sent_tokenize(metin)
# metin_n = metin.replace('n', 't')
print("-"*100)
yeni_metin = []
for i in butun_sozcukler:
    yeni_metin.append([len(i), i])


for k in yeni_metin:
    print(k, "---")
print(yeni_metin[12])
print(len(yeni_metin)) # 1427 tane sözcük var.
print (len(metin)) # 6389 karakter uzunluğunda.





