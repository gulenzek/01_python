# Q3
# def alti_cizili_yaz(baslik, karakter):
#     print(baslik)
#     print(len(baslik) * karakter)
#
#
# ahmet
# _____

def alti_cizili_yaz(baslik, karakter="_"): #altına yazacağı karakteri default olarak veriyoruz.
    sonuc = ""
    sonuc = sonuc + baslik + "\n"
    sonuc = sonuc + (karakter * len(baslik))
    return sonuc

print(alti_cizili_yaz("ahmet", "_"))
