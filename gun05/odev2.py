# Q2 stars
# def print_stars(num):
#     pass
#
# 1 için:
# *
#
# 2 için:
# *
# **
#
# 3 için:
# *
# **
# ***

def print_stars(num: int):
    """
    num sayısı kadar yıldız yazdıran program.
    :param num:integer değer alıyor.
    :return: string değer döndürüyor.
    """
    sonuc = ""
    for rakam in range(num):
        sonuc = sonuc + str(rakam + 1) + " için:\n"
        sonuc = sonuc + ("*" * (1 + rakam)) + "\n"
    return sonuc


print(print_stars(9))
