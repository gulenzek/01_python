x = "merhaba"
y = "nasılsın?"
name = "Zeki"
#

print(f"{name}, nasılsın! {x}")

def middlesprint(string1):
    """
    mina
    :param string1:
    :return:
    """
    string2 = string1.replace(" ", "")
    # baslik = "\tstring2\t"

    return baslik


def middlestrip2(yazi):
    """
    adil

    ileride, \t\n karakterleri de dikkate alinabilir.

    :param yazi:
    :return:
    """
    toplamkaraktersayisi = len(yazi)
    yazi1 = yazi.strip()
    a = yazi.rstrip()
    sagdanbosluksuzkaraktersayisi = len(a)
    b = yazi.lstrip()
    soldanbosluksuzkaraktersayisi = len(b)
    bosluksuz = yazi1.replace(" ", "")
    # len(bosluksuz)
    soldan_karakter_sayisi = toplamkaraktersayisi - soldanbosluksuzkaraktersayisi
    sagdan_karakter_sayisi = toplamkaraktersayisi - sagdanbosluksuzkaraktersayisi
    solbosluk = (soldan_karakter_sayisi * " ")
    sagbosluk = (sagdan_karakter_sayisi * " ")
    sonuc = solbosluk + bosluksuz + sagbosluk
    return sonuc


def middlestrip3(lakirti):
    """
    Q1
    @author: Zeki Gülen, 17/10/2020

    terim = "            a b  "
    terim1 = "  A \n  a d@  1  2 \t"
    terim2 = "   aa b c   "

    print(middlestrip3(terim))
    print(middlestrip3(terim1))
    print(middlestrip3(terim2))
    """
    return (len(lakirti) - len(lakirti.lstrip())) * " " + "".join(lakirti.split()) + (
                len(lakirti) - len(lakirti.rstrip())) * " "



def print_stars(num):
    star_count = []
    for num in star_count:
        star_count[num] = star_count.count(num, 0) + 1
        print(num)
        print(star_count[num] * "*")

def print_stars2(max_star_count):
    """
    1 için:
        *
    3 için:
        *
        **
        ***
    :param max_star_count:
    :return:
    """
    for num in range(1, max_star_count+1):
        # print(num)
        # print("*" * num)
        for j in range(num):
            # print("*", end="\n")
            print("*", end="")
        print()


def join_ornegi():
    # join, split'in karsiti gibi dusunebiliriz.
    str1 = "a b c d e    f"
    parts = str1.split()

    str2 = "//".join(parts)

    print()


def kelimelik(kelime, karakter="_"):
    """
    Serdar.

    kelime = "ahmetsdfsdf"
    print(kelimelik(kelime))
    """
    sayac = 0
    for harf in kelime:
        sayac += 1
    print(kelime)
    print(sayac * karakter)
    return sayac

kelime = "ahmetsdfsdf"
kelimelik(kelime)
kelime = "ahmetsdfsdf"
kelimelik(kelime, "*")


def main():
    a = 4
    b = 2
    # cok karmasik islemler
    c = a + b
    assert c >= 6

    # print(middlestrip2("  tahta "))
    sonuc = middlestrip2(str("  tahta\t kurusu\t "))
    # assert sonuc == "  tahtakurusu\t "
    # print_stars2(5)
    join_ornegi()

    # str.ljust(width[, fillchar])
    str1 = "tahta"
    str2 = str1.ljust(10, "_")  # tahta_____
    str2 = str1.rjust(10, "_")  # _____tahta
    print(str2)

    a = 4
    b = 8
    toplam = a + b
    # f-strings: formatted strings
    print(f"{a} ile {b} sayisinin toplami: {toplam}")
    print("{} ile {} sayisinin toplami: {}".format(a, b, toplam))

# main()

assert isinstance(kelime, str) # kelimenin string olmasını söylüyor.


