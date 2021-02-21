# -*- coding: utf-8 -*-
"""

"""


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
        # instance method, cunku self aliyor.
        pass

    @staticmethod
    def team_capitalize(str1):
        """
        kucuk harfli yazilmis takim adini buyutur.
        sanki class'in altina yazilmis gibi dusunelim.
        :param self:
        :return:
        """
        pass


def main():
    m1 = Match("england", "scotland", 4, 2)
    m1.draw()  # self'e m1 gelir.

    m2 = Match("germany", "italy", 3, 1)
    m2.draw()  # self'e m1 gelir.

    m1.team_capitalize("herhangi bir string")  # Python, m1'de olmadigi icin, Match'dekini cagiriyor.

    # dogrusu bu, Match class icindeki calisir:
    Match.team_capitalize()


if __name__ == "__main__":
    main()
