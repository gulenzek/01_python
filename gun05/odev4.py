# Q4
# # Bir sayıya kadar olan sayıların toplamını döndüren bir fonksiyon yazınız.
#
# def sum_up_to(number):
#     pass
#
# sum = n(n+1)/2

def toplam(sayi):
    """
    Belirli bir sayıya kadar toplam bulma.
    :param sayi:
    :return:
    """
    sayi = sayi*(sayi+1)/2
    return sayi

print(toplam(10))