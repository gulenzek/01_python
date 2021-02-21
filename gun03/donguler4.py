import random

numbers = []
while True:
    number1 = random.randint(1,60)
    if number1 not in numbers:
        numbers.append(number1)
        if len(numbers)==50:
            break

print(numbers)


# 50 tane random sayi uretelim.
# bu sayilari bir listede toplayalim.
# ama icinde tekrar olmasin.

import random

numbers = []
while True:
    number1 = random.randint(1, 100)
    if number1 not in numbers:
        numbers.append(number1)
    if len(numbers) == 50:
        break
print(numbers)


# kesir sadelestirme
# 40/100 -> 2/5


print(10%3, "__")


# x = +1/1 - 1/2 + 1/4 - 1/8 + 1/16 - 1/32
result = 0
for i in range(0, 100):
    payda = 2 ** i
    if i % 2 == 0:
        # 0, 2, 4 +
        result += 1/payda
    else:
        # -
        result += -(1/payda)
print(result)
