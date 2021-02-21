# Q6
# s = 1 + 2/3 + 4/9 + 8/27 + ...
# şeklinde bir seri tanımlı olsun.
# ilk 100 terimin toplamı nedir?

# s = 1 + 2/3 + 4/9 + 8/27
#    0    1     2     3 ...
# @author: Zeki Gülen, 16/10/2020

def iki_bolu_ucun_ussu(ussu: int):
    """
    2/3'ün üssünü alarak belirtilen rakama kadar bu üsleri toplayan bir fonksiyondur.
    :param ussu:
    :return:
    """
    toplam = 0
    for i in range(ussu):
        toplam += (2 / 3) ** i
    return toplam


print(iki_bolu_ucun_ussu(100))
