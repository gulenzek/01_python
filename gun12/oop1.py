# -*- coding: utf-8 -*-
"""
oop1.py

static method
class method
"""


class Renk:
    red = "kirmizi"
    green = "yesil"
    blue = "mavi"


class Match:
    # bunlardan 1er tane var:
    points_for_win = 3
    points_for_draw = 1

    def __init__(self, hometeam, awayteam, homeft, awayft):
        # instance attribute, bunlardan 38000 tane var.
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.homeft = homeft
        self.awayft = awayft

        # bunlar, instance attribute olmamali:
        # self'a bagli olmamali.
        # self.points_for_win = 3
        # self.points_for_draw = 1

    def draw(self):
        pass

    def home_win(self):
        pass

    def away_win(self):
        pass


def main():
    m1 = Match("england", "scotland", 4, 2)
    m1.home_win()  # self'e m1 gelir.

    m2 = Match("germany", "italy", 3, 1)
    m2.home_win()  # self'e m1 gelir.

    print(Match.points_for_draw)  # 1
    print(Match.points_for_win)  # 3

    # class atribute'lara, object uzerinden erisim:
    # bunu da yapmayin.
    print(m1.points_for_draw)  # 1
    print(m1.points_for_win)  # 3

    print(id(Match.points_for_draw))  # 140721439323936
    print(id(m1.points_for_draw))  # 140721439323936

    Match.points_for_win = 4

    print(Match.points_for_win)  # 4
    print(m1.points_for_win)  # 4
    print(m2.points_for_win)  # 4

    m1.taraftar_sayisi = 50000
    #  W0201: Attribute 'taraftar_sayisi' defined outside __init__ (attribute-defined-outside-init)
    # bunu yapmayin.

    m1.points_for_win = 5
    # m1 icin ayri bir points_for_win tanimladi.
    # self icinde, instance attribute oldu.
    # bunu da yapmayin.

    print(Match.points_for_win)  # 4
    print(m1.points_for_win)  # 5 ????
    print(m2.points_for_win)  # 4

    print(id(Match.points_for_win))  # 140721989957504
    print(id(m1.points_for_win))  # 140721989957536 ????
    print(id(m2.points_for_win))  # 140721989957504


if __name__ == "__main__":
    main()
