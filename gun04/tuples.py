# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("kadınım")
x = tuple(y)

print(x)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple4 = ("karpuz", )

tuple3 = tuple1 + tuple2 + tuple4
print(tuple3)

fruits = ("apple", "banana", "cherry", "muz", "şeftali")
print(fruits[3])
# fruits[2] = "vişne" # TypeError: 'tuple' object does not support item assignment

# fruits[5] = "karpuz" # This will raise an error. TypeError - ekleme
print(len(fruits))

thistuple2 = ("karpuz",) # virgülün önemi.. :)


