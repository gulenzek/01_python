# -*- coding: utf-8 -*-
"""

"""


def main():
    takimlar = ["england", "scotland", "wales"]
    puanlar = ["18", "22", "13"]
    zipped = zip(takimlar, puanlar)  # zip object
    zipped2 = list(zip(takimlar, puanlar))

    total = 0
    for item in zipped2:
        # print(item)
        # puanina nasil ulasiriz?
        puan = int(item[1])
        total += puan

    # total2 = sum(puanlar)  # string ile calismadi.
    total2 = sum([int(x) for x in puanlar])
    print(max(takimlar))  # string uzerinde de calisti.

    print(zipped2[0][1])
    print(total)
    print(total2)


if __name__ == "__main__":
    main()
