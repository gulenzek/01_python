# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
Bir geometrik şekil olan dairenin sınıfıdır. Yarıçapının alıyoruz.
"""


class Daire:
    def __init__(self, yaricap: float):
        self.yaricap = yaricap

    def __str__(self):
        return "Bu yarıçapı {} olan bir dairedir.".format(self.yaricap)

    def alan

def main():
    d1 = Daire(3)
    print(d1)
    pass


if __name__ == "__main__":
    main()
