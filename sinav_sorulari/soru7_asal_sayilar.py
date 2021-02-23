# author: gulenzek

def asal_sayilar(n):
    asal_sayi = []

    for i in range(2,n+1):
        bolundu = False         # neden?
        for j in range(2,i):
            if i%j == 0:
                bolundu = True
        if bolundu == False:
            asal_sayi.append(i)
    return asal_sayi

print(asal_sayilar(200))