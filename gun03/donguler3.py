# donguler3.py
# histogram

# str1 = "quick fox jumped over the dog"
#
#
# histogram = {}
#
# for harf in str1:
#     histogram[harf] = histogram.get(harf, 0) + 1
#
# print(histogram)


# idiom DİKKAT! "python idioms" diye aratabiliriz.


tam_bolenler = []
sayi = 0
while True:
    sayi = int(input(">>>"))
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            tam_bolenler.append(i)
    print(tam_bolenler)


# not
# donguler3.py

# histogram
str1 = "quick fox jumped over lazy dog"
str1 = str1.replace(" ", "")

histogram = {}
for harf in str1:
    # idiom:
    # if harf in histogram:
    #     histogram[harf] = histogram[harf] + 1
    # else:
    #     histogram[harf] = 1

    # ustteki satirlari yazmak yerine:
    histogram[harf] = histogram.get(harf, 0) + 1

print(histogram)


# bir tam sayinin tam bolenleri
# >>>2
# [1, 2]
# >>>3
# [1, 3]
# >>>8
# [1, 2, 4, 8]
# >>>9
# [1, 3, 9]

sayi = 0
tam_bolenler = []
# sayi = int(input(">>>"))
sayi = 3
for i in range(1, sayi//2+1):
    if (sayi%i==0):
        tam_bolenler.append(i)
tam_bolenler.append(sayi)
print(tam_bolenler)



#____________________________________________________________
# donguler3.py

# histogram
str1 = "quick fox jumped over lazy dog"
str1 = str1.replace(" ", "")

histogram = {}
for harf in str1:
    # idiom:
    # if harf in histogram:
    #     histogram[harf] = histogram[harf] + 1
    # else:
    #     histogram[harf] = 1

    # ustteki satirlari yazmak yerine:
    histogram[harf] = histogram.get(harf, 0) + 1

print(histogram)

# bir tam sayinin tam bolenleri
# >>>2
# [1, 2]
# >>>3
# [1, 3]
# >>>8
# [1, 2, 4, 8]
# >>>9
# [1, 3, 9]

sayi = 0
tam_bolenler = []
# sayi = int(input(">>>"))
sayi = 3
for i in range(1, sayi // 2 + 1):
    if sayi % i == 0:
        tam_bolenler.append(i)
tam_bolenler.append(sayi)
print(tam_bolenler)


# palindrome.
# tersine cevirildigi zaman degismeyen kelimeler.
# YATAY, ADA
str1 = "yatay"
str2 = "bacxab"

str1_r = str1[::-1]
# [::-1] list ve str'lerde calisir.
print(str1_r)
if str1 == str1_r:
    print("palindrome")
else:
    print("palindrome degil.")

# Alihan
word = "xaaZax"
isPalindrome = True
for i in range(0, len(word) // 2):
    soldan = word[i]
    sagdan = word[((len(word) - 1) - i)]
    if soldan != sagdan:
        # if word[i] != word[((len(word) - 1) - i)]:
        isPalindrome = False
        break
print(isPalindrome)


# Palindrom kelimeler
# @Zeki Gülen, 15/10/2020
# palindrom = input(">>>")
palindrom = "xaamaax"
str1 = ""
for i in palindrom:
    str1 = i + str1
if palindrom == str1:
    print("palindrom")
else:
    print("değil")


# factorial
# n! = n * (n-1) * (n-2) .. 1
# 0! = 1
# 1! = 1

n = 5
toplam = 1
for i in range(n, 0, -1):
    toplam = toplam * i
    print(i)
print(toplam)
