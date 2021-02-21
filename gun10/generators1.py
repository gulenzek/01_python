# -*- coding: utf-8 -*-
"""
generators1.py
"""


def city_generator():
    yield "istanbul"
    yield "kastamonu"
    yield "sivas"


city1 = city_generator()
print(next(city1))
print(next(city1))
print(next(city1))


# print(next(city1))  # StopIteration
# print(next(city1))

def countdown(n):
    while n > 0:
        n = n - 1
        # print(n)
        yield n


# countdown(5)
for num in countdown(5):
    print(num, "__")

gen1 = countdown(6)
print(next(gen1))  # 5
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))  # 0
# print(next(gen1))  # StopIteration


gen2 = countdown(6)
items = list(gen2)
print(items)  # [5, 4, 3, 2, 1, 0]
