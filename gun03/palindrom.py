# Palindrom kelimeler
# @Zeki Gülen, 15/10/2020
palindrom = input(">>>")
str1 = ""
for harf in palindrom:
    str1 = harf + str1

if palindrom == str1:
    print("palindrom")
else:
    print("değil")
    print(str1)
