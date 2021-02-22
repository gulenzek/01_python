# author: @gulenzek
paragraf = "merhaba dünya. merhaba admin dilerim merhaba "
def kelime_say(para):
    sozcukler = {}
    for sozcuk in para.split():
        if sozcuk not in sozcukler:
            sozcukler[sozcuk] =1
        else:
            sozcukler[sozcuk] += 1
    return sozcukler

print(kelime_say(paragraf))
