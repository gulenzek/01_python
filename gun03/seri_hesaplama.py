# x = 1 - 1/2 + 1/4 - 1/8 + 1/16 -1/32


sayi = 2**0 - 2**-1 + 2**-2 - 2**-3 + 2**-4 - 2**-5
print(sayi)


# x = +1/1 - 1/2 + 1/4 - 1/8 + 1/16 - 1/32
n = 32
result =0
for us in range(0, 6):
    payda = 2 ** us
    if us % 2 == 0:
        result += 1/payda
    else:
        result += -1/payda
    print(payda)
print(result)