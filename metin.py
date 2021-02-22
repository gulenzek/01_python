# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run 
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
