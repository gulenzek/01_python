# bir str'nin harflerinden kaç tane olduğunu gösteren bir grafik çizer.

def histogram_ciz(word):
    harfler = {}
    for harf in word:
        harfler[harf] = harfler.get(harf, 0) + 1
        print(harfler)

    karakter = "*"
    for harf in harfler:
        print(harfler.get(), harfler.get(harf), harfler.get(harf) * karakter)

    print(harfler)

histogram_ciz("zeki gulen")

print(histogram_ciz.__code__.co_nlocals)
