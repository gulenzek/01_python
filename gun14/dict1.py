# -*- coding: utf-8 -*-
"""

"""

import collections

def main():
    numbers = {}
    numbers["bir"] = "one"
    numbers["iki"] = "two"
    numbers["uc"] = "tree"

    colors = {}
    colors["mavi"] = "blue"
    colors["yesil"] = "green"
    colors["kirmizi"] = "red"

    del colors["yesil"]  # O(1)
    print(colors)
    # {'mavi': 'blue', 'kirmizi': 'red'}

    print(colors["mavi"])  # get islemi, O(1)
    colors["turuncu"] = "orange"  # set islemi, O(1)


    # numbers["iki"] = "two"
    colors["iki"] = "2"

    # set
    set1 = {7, 5, 8}
    list1 = [4, 7, 2, 8]
    set2 = set(list1)

    map1 = collections.ChainMap(numbers, colors)
    print(map1["bir"])
    print(map1["turuncu"])
    print(map1["iki"])  # numbers["iki"] = "two"
    # bulunca cikti, colors icinde de "iki" olmasina ragmen ilkinde buldu.

    car_name = "koenigsegg agera rs"
    counter1 = collections.Counter(car_name)
    for letter in counter1:
        print(letter, counter1[letter])

    # LIFO  last in, first out (Turkiye)
    # FIFO first in, first out (Norvec, Isvicre)
    deq1 = collections.deque()
    deq1.append("a")
    deq1.append("b")
    deq1.append("c")

    left_element = deq1.popleft()

    left_element2 = deq1.popleft()
    # bu sekilde bir kullanim, FIFO oldu.

    # stack, last in, first out
    stack1 = collections.deque()
    stack1.append("a")
    stack1.append("b")
    stack1.append("c")

    item1 = stack1.pop()  # c
    item2 = stack1.pop()  # b

    print()


if __name__ == "__main__":
    main()
