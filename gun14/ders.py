# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""

import collections

list1 = ["a", "b", "c"]
list1.append("d") # O(1)
list1.insert(1, "x")  # O(n)

numbers = {}

colors = {}
colors["mavi"] = "blue"
colors["yesil"] = "green"
colors["kirmizi"] = "red"

del(colors["yesil"]) # O(1)

print(colors)

print(colors["mavi"]) # get işlemi O(1)

colors["turuncu"] = "orange" #set işlemi O(1)
def main():
    pass


if __name__ == "__main__":
    main()

car_name = "merhaba"
counter1 = collections.Counter(car_name)

for letter in counter1:
    print(letter, counter1[letter])


collections.deque  # double ended queue


# Stack, LIFO

stack1 = collections.deque

stack1.append("1")
stack1.append("2")
stack1.append("3")

item1 = stack1.pop()
item2 = stack1.pop()

print (item1, item2)

dict.get("eleman", None veya 0)

renkler = collections.defaultdict


import enum

import random

def random_list(n):
