# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
def uniques_only(iterable1):
    Bir liste ya da tuple içindeki elemanlarin tekil olmayanlari atilmis halini donduren fonksiyon.
    işlem sonrasında, sıralama bozulmamalidir.
    [7, 6, 7, 2, 9, 2, 1] -> [7, 6, 2, 9, 1]
    assert isinstance(iterable1, (list, tuple))
    # TODO: implement uniques_only(iterable1)
"""


def uniques_only(iterable1):
    iterable2 = []
    for i in iterable1:
        if i % 2 == 0:
            ""
        else:
            iterable2.append(i)

    return iterable2


print(uniques_only([7, 6, 7, 2, 9, 2, 1]))
print(uniques_only((7, 6, 7, 2, 9, 2, 1)))
