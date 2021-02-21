# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""
from urllib.request import urlopen


def main():
    url = r"http://www.tcmb.gov.tr/kurlar/today.xml"
    handle = urlopen(url)
    print(url)
    print(handle)
    pass


if __name__ == "__main__":
    main()
