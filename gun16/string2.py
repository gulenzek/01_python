# -*- coding: utf-8 -*-
"""

"""

import string


def validate_pwd(s, buyuk_harf_sayisi=2):
    def is_punc(c):
        return c in string.punctuation

    if len(s) < 8:
        return False
    if sum(map(str.isupper, s)) < buyuk_harf_sayisi:
        return False
    if sum(map(str.isdigit, s)) < 2:
        return False
    if sum(map(is_punc, s)) < 1:
        return False
    # Note of the tests have been violated, return True
    return True


def isValidTCID(value):
    value = str(value)

    # 11 hanelidir.
    if not len(value) == 11:
        return False

    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False

    # Ilk hanesi 0 olamaz.
    if int(value[0]) == 0:
        return False

    digits = [int(d) for d in str(value)]

    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return False

    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
    # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False

    # Butun kontrollerden gecti.
    return True


yazi = str(input("yazı giriniz: "))


def middlestrip(yazi):
    """

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
    len(bosluksuz)
    c = toplamkaraktersayisi - soldanbosluksuzkaraktersayisi
    d = toplamkaraktersayisi - sagdanbosluksuzkaraktersayisi
    solbosluk = (c * " ")
    sagbosluk = (d * " ")
    sonuc = solbosluk + bosluksuz + sagbosluk
    return sonuc


def main():
    pass


if __name__ == "__main__":
    main()
