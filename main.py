print("merhaba")

pi = 3.14
# assignment, atama

cevap = 42
x, y = 4, 5

a = 4
b = a + 2
a = 10
# b -> 12

# type inference
print(type(pi))  # 3.14 <class 'float'>
print(type(cevap))  # 42 <class 'int'>
print(type(23.45))  # <class 'float'>
print(type("merhaba"))  # <class 'str'>

n6 = 6
print(n6)
# NameError: name 'n6' is not defined

print()
# SyntaxError: unmatched ')'

# sayisal degiskenlerin boyutu.
# int, long, int64
# float, double

n1 = 862354826788623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892378623548267891274682364892379127468236489237
print(n1)

f1 = 34536345345345345.123453453435
print(f1)

n2 = 64**64
print(n2)

c1 = 3+5j
print(c1)
print(type(c1))  # <class 'complex'>

# stringler.
str1 = "batman the dark knight"
str2 = 'batman the dark knight'
print(type(str1))  # <class 'str'>

# batman's revenge "the justice night"

str3 = "batman's revenge"
str4 = "batman's revenge \"the justice night\""
# / bolu, slash
# \ backslash

dosya_adi = "c:\\taramalar\\resim1.png"
# c:	aramalar\esim1.png
# c:\taramalar\resim1.png
print(dosya_adi)  # esim1.png

dosya_adi2 = r"c:\taramalar\resim1.png"
# bastaki r, raw_string

sayilar = "1\n2\n3\n4\n"
print(sayilar)

backslash_karakterleri = r"""
\\	Backslash (\)
\'	Single quote (')
\"	Double quote (")
\n	ASCII Linefeed (LF)
\r	ASCII Carriage Return (CR)
\t	ASCII Horizontal Tab (TAB)
"""
print(backslash_karakterleri)


# index ile erisim.
#     01234567
s1 = "superman"

print(s1[0])  # s
print(s1[3])  # e
print(len(s1))  # 8

# son karakterini alalim.
film1 = "batman"
film2 = "in time"
print(film1[len(film1)-1])  # n
print(film2[len(film2)-1])  # e
print(film1[-1])  # n  # reverse index
print(film1[-2])  # a

kelime1 = film2[0] + film2[1]
print(kelime1)

# slicing, dilimleme
kelime2 = film2[0:5]  # 0 dahil, 5 dahil degil.
print(kelime2)  # "in ti"

kelime3 = film2[0:2]
print(kelime3)

#   7654321
#   in time
kelime4 = film2[-4:-1]  # tim
kelime4 = film2[-4:]  # time
print(kelime4)

k5 = film2[:4]  # "in t"
print(k5)

k6 = film2[:]  # tam kopyasi

# orthagonal


# Arithmetic Operators(+ - * / ** % //)
print(4+5)
n1 = 6-2

print(5/2)  # 2.5, true division
print(5//2)  # 2, integer division, floor division
print(2**3)  # 8
print(5%2)  # bolumden kalani: 1

# print(1/0)  # ZeroDivisionError

print(4 + 5)
print(4 * 5)
# print(4 + "a")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# operator: +
# operands: 4, "a"

print("-" * 20)  # --------------------


# yeni string olusturmak.
# var olan bir string'i degistirmek.
# str: alfanumerik deger, karakter dizisi, katar
film3 = "avengers"
# film3[0] = "A"
# TypeError: 'str' object does not support item assignment
# mutable(degisebilir), immutable
# string: immutable
film4 = "A" + film3[1:]
print(film4)


# string'ler
# dir()  -> directory
print(dir(film4))
# film3 == "avengers"
film5 = film3.capitalize()  # Avengers
film5 = film3.upper()  # AVENGERS
kac_tane = film3.count("e")
print(kac_tane)  # 2
print(film5)

baslik = film3.center(20, "_")
print(baslik)

# upper() lower()
# strip(), lstrip(), rstrip()
film6 = "   the avengers  "
print(film6.lstrip())  # left strip, "the avengers  "
print(film6.rstrip())  # right strip "   the avengers"
print(film6.strip())  # left and right "the avengers"

film7 = film6.replace(" ", "_")  # ___the_avengers__
print(film7)

print("3453".isdigit())  # True
print("345a3".isdigit())  # False

# chaining
s1 = "   the avengers  "
s2 = s1.upper().strip().center(40)
print(s2)


# kullanicidan deger almak.
# deger = input("bir diger giriniz:")
# print(deger)


# problem:
# kullaniciya adini sorup,
# merhaba Ahmet seklinde bir cikti veren bir program yaziniz.
# deger = input("Adınız:")
# print("Merhaba " + deger)


# kullanicindan 2 sayi alip,
# bu 2 sayini toplamini yazan bir program.
number1 = int(input("number1:"))
number2 = int(input("number2:"))
toplam = number1 + number2  # 45
# toplam = int(number1) + int(number2)  # 45
print(toplam)
# concatenation, uc uca eklemek.
