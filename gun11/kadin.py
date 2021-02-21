# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""


class Kadin:
    def __init__(self):
        self._ad = {}
        self._soyad = {}

    def ad_koy(self, ad, soyad):
        self._ad = ad
        self._soyad = soyad

    def __setitem__(self, key, value):
        self.ad_koy(ad=key, soyad=value)


def main():
    pass


if __name__ == "__main__":
    main()
