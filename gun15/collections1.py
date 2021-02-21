# -*- coding: utf-8 -*-
"""

"""

import collections
import enum


class Color(enum.Enum):
    red = 1
    blue = 2
    green = 3


def do_enum():
    print(Color.red)  # 1, Color.red
    print(Color.red.value)  # 1
    print(Color(1))  # Color.red


def do_chain_map():
    numbers = {}
    numbers["bir"] = {"ingilizce": "one", "rakam": 1}
    numbers["iki"] = "two"
    numbers["uc"] = "tree"

    colors = {}
    colors["mavi"] = "blue"
    colors["yesil"] = "green"
    colors["kirmizi"] = "red"
    colors["bir"] = "1color"

    map1 = collections.ChainMap(numbers, colors)
    # map1 = collections.ChainMap(colors, numbers)  # farkli sonuc verir.
    print(map1["iki"])
    print(map1["yesil"])
    print(map1["bir"])  # ??
    print(len(map1))  # 6
    print()


def do_counter():
    car_name = "koenigsegg agera rs"
    counter1 = collections.Counter(car_name)
    for letter in counter1:
        freq = counter1[letter]
        print(letter, freq)


def do_queue():
    deq1 = collections.deque(["a", "b", "c", "d"])

    # LIFO  last in, first out (Turkiye)
    # son giren, ilk cikar
    deq1.append("e")  # O(1)
    deq1.append("f")  # O(1)
    print(deq1)  # deque(['a', 'b', 'c', 'd', 'e', 'f'])
    # LIFO: stack mantigi.

    item1 = deq1.pop()  # f, O(1)
    item2 = deq1.pop()  # e, O(1)

    # FIFO first in, first out (Norvec, Isvicre)
    # ilk giren, ilk cikar.
    item3 = deq1.popleft()  # O(1)
    item4 = deq1.popleft()  # O(1)

    print()


def default_color():
    return None


def do_default_dict():
    dd1 = collections.defaultdict(default_color)

    # defaultdict(default_factory[, ...]) –> dict with default factory
    # The default factory is called without arguments to produce a new value
    # when a key is not present, in __getitem__ only

    dd1["red"] = "kirmizi"
    dd1["blue"] = "mavi"
    print(dd1["red"])  # kirmizi

    print(dd1["orange"])  # None
    # dd1.get("orange", None)

    # bu sekilde de yazilan kodlar var:
    # dd1 = collections.defaultdict(int)
    dd1["olmayan_renk"] = int()


def do_named_tuple():
    Point = collections.namedtuple("Point", ["x", "y"])
    Championship = collections.namedtuple("Championship", ["driver", "car", "manufacturer"])
    ch1 = Championship("juha kankunen", "lancia delta integrale HF", "Lancia")
    print(ch1[1])  # normal tuple index ile erisim
    print(ch1.car)  # ayni elemana, isim ile erisim.


def main():
    # do_chain_map()
    # do_counter()
    # do_queue()
    # do_default_dict()
    # do_named_tuple()
    do_enum()


if __name__ == "__main__":
    main()
