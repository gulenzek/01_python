# Q8 shout()
# •	shout isimli bir fonksiyon yazınız.
# •	Bu fonksiyon:
# •	string tipinden bir parametre almalıdır.
# •	her karakteri büyük harfe çevirmelıdır.
# •	her karakterin arasina bir boşluk koymalıdır.
# •	sonuna da ünlem eklemelidir.
# # Uygulama: shout()
#
# def shout(needle):
#     """
#     strip()
#     hersey uppercase
#     her bir karakter arasina bir " " koysun.
#     sonunda da unlem yoksa eklesin.
#
#     "no i will not": "N O  I  W I L L  N O T !"
#     :type needle: str
#     :param needle:
#     :return:
#     """

def shout(terim):
    sonuc = ""
    for i in terim:
        sonuc += str(i).upper() + " "
    if sonuc[len(sonuc) - 2] != "!":
        sonuc += "!"
    return sonuc


print(shout(input(">>>")))

