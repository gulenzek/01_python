# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
ç - c
Ç - C
ğ - g
Ğ - Ğ
ı - i
İ - I
ö - o
Ö - O
ş - s
Ş - S
ü - u
Ü - U
"""
def ascii_tr(text):
    text1 = text.replace("ç", "c")
    text2 = text1.replace("Ç", "C")
    text3 = text2.replace("ğ", "g")
    text4 = text3.replace("Ğ", "G")
    text5 = text4.replace("ı", "i")
    text6 = text5.replace("İ", "I")
    text7 = text6.replace("ö", "o")
    text8 = text7.replace("Ö", "O")
    text9 = text8.replace("ş", "s")
    text10 = text9.replace("Ş", "S")
    text11 = text10.replace("ü", "u")
    text12 = text11.replace("Ü", "U")
    return text12

def main():
    meraba = ascii_tr("şanlıürfİ")
    print(meraba)


if __name__ == "__main__":
    main()
