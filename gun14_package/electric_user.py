# -*- coding: utf-8 -*-
"""

"""
# from electric import voltage
import electric

# import sympy.physics.units as units
# units.voltage
# from physics import atislar
import physics  # physics.__init__.py import olur.


def main():
    # v1 = voltage(2, 3)  # from electric import voltage
    v1 = electric.voltage(4, 5)
    print(v1)
    physics.atislar.egik_at(3, 5)
    physics.vektor_carp()  # __init__.py'de oldugu icin.


if __name__ == "__main__":
    main()
