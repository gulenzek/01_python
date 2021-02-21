# -*- coding: utf-8 -*-
"""

"""

var1 = 18

def main():
    global var1
    var1 = 19
    print(var1, "___2")  # 19

    local1 = 22

    local_vars = locals()
    global_vars = globals()

    print(local_vars)
    print(global_vars)
    # print(main.__code__.co_nlocals)  # 3


if __name__ == "__main__":
    print(var1, "___1")  # 18
    main()
    print(var1, "___3")  # 18 ??
    # 19 yazmasini isteseydik?

