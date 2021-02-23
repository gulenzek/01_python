# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""


def main():
    list1 = ["a", "b", ("c", "d")]
    list1 = list1.append("e")
    print(len(list1)) # TypeError: object of type 'NoneType' has no len()
    # list1 append fonksiyonu None döndürdüğü için list1 = None olur. Ondan dolayı None olan bir object'in len()'i olmaz.

if __name__ == "__main__":
    main()
