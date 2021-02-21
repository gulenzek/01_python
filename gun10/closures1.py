# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
closures1.py
"""

# scope / kapsam kısmını irdeleyelim..

def is_strong_password(password):
    password_chars = "abcx"
    # is_punc("a") is not defined
    def is_punc(letter):
        return True
    is_punc("b") # üstte tanımlandığı için çağırabiliyoruz..

print(is_strong_password("abc"))
# print(is_punc("abc")) # NameError: name 'is_punc' is not defined


def selamlayici(kok):
    def inner_function(isim):
        print(kok, isim)
    return inner_function # çağırmak değil, pointer.. dikkat dikkat..