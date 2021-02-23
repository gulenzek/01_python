# -*- --coding:utf-8 -*-
# @author: gulenzek
"""

"""


def main():
    tickets = {"Barcelona": 250, "Paris": 200, "Atina": 50}
    tickets.append({"Atina": 55})
    print(tickets)      # AttributeError: 'dict' object has no attribute 'append'

if __name__ == "__main__":
    main()
