# -*- coding: utf-8 -*-
"""

"""

import shelve

def do_shelve():
    boston_celtics = {}
    boston_celtics["name"] = "boston celtics"
    boston_celtics["win"] = 17
    boston_celtics["loss"] = 4
    boston_celtics["years_won"] = [1957, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1968, 1969, 1974, 1976, 1981,
                                   1984, 1986, 2008]

    chicago_bulls = {}
    chicago_bulls["name"] = "chicago bulls"
    chicago_bulls["win"] = 6
    chicago_bulls["loss"] = 0
    chicago_bulls["years_won"] = [1991, 1992, 1993, 1996, 1997, 1998]

    file_name = "nba.db"  # nba.shelve de olabilirdi.
    handle = open(file_name)
    handle["boston_celtics"] = boston_celtics
    handle["chicago_bulls"] = chicago_bulls
    handle.close()

def main():
    pass


if __name__ == "__main__":
    main()
