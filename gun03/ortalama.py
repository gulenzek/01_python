# utf-8
# @author: Zeki Gülen

toplam = 0
count = 0
puan = 0
while True:
    deger = input(">>>").strip()
    if deger.isdigit():
        puan = int(deger)
    else:
        print("lütfen bir sayı giriniz.")
        continue

    toplam = toplam + puan
    count += 1
    print(toplam)

print(toplam/count)

# Alihan

total = 0
count = 0
while True:
    num = input("Give a number: ").strip()
    if num[0] == "-" and num[1:].isdigit():
        break
    elif num.isdigit():
        num = int(num)
        total += num
        count += 1
    else:
        print("Invalid value")
        print()
print(total / count)
