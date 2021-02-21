# -*- coding: utf-8 -*-
"""
data_structures2.py
"""

import collections
import enum

class Color(enum.Enum):
    red = 1
    green = 2
    blue = 3

def use_color():
    print(Color.red)  # Color.red
    print(Color(1))  # Color.red
    print(Color.red.value)  # 1

    # dogal olarak bu da gecerli:
    print(Color(1).value)  # 1

    for color in Color:
        print(color)

def default_color():
    return None

def main():
    dict1 = {}
    # print(dict1["eleman"])  # KeyError: 'eleman'
    temp = dict1.get("eleman", None)

    renkler = collections.defaultdict(default_color)
    renkler["kirmizi"] = "red"
    renkler["yesil"] = "green"

    print(renkler["kirmizi"])
    print(renkler["turuncu"])

    # bu yine KeyError verecektir:
    # print(dict1["olmayan_eleman"])

    Point = collections.namedtuple("Point", ["x", "y"])
    p1 = Point(4, 6)
    print(p1.x)  # 4
    print(p1.y)  # 6

    p2 = (4, 6)

    Kisi = collections.namedtuple("Kisi", ["adi", "soyadi", "tc_kimlik_no"])
    k1 = Kisi("ahmet", "tuncay", 125)
    print(k1.soyadi)
    print(k1[0])  # ahmet

    use_color()


if __name__ == "__main__":
    main()
