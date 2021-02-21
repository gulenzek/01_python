# -*- coding: utf-8 -*-
"""
oop_vektor.py

# stack trace
"""

class UyumsuzVektorError(Exception):
    """
    kullanim:
    raise UyumsuzVektorError("hic bir eleman None olamaz.")

    https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    """
    def __init__(self, message):
        self.message = message


class Vektor:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x{self.x} y{self.y} z{self.z}"

    def __add__(self, other):
        try:
            x_total = self.x + other.x
            y_total = self.y + other.y
            z_total = self.z + other.z
            handle = open("sonuclar.txt", "w", encoding="utf8")
            # TODO: yaz, islemler yap
            handle.close()
        except TypeError:
            # raise TypeError("hic bir eleman None olamaz.")
            raise UyumsuzVektorError("hic bir eleman None olamaz.")
        except FileNotFoundError:
            # admine_mail_at()
            raise  # son hatayi tekrar firlatir.

        vnew = Vektor(x_total, y_total, z_total)
        return vnew


def main():
    v1 = Vektor(1, 2, 3)
    v2 = Vektor(5, 6, 7)
    v3 = v1 + v2
    print(v3)

    # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
    v4 = Vektor(1, 2, 3)
    v5 = Vektor(5, 6)
    v6 = v4 + v5


if __name__ == "__main__":
    main()
