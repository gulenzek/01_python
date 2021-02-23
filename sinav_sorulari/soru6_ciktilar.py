# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""


def main():
    i = 1
    while True:
        if i == 5:
            i = i + 3
            continue
        elif i % 8 == 0:
            print(8)
            break
        print(i, end="_")   # 1_2_3_4_8
        i += 1


if __name__ == "__main__":
    main()
