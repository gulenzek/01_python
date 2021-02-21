# list_comprehensions.py
# tuple ve set icin de uygulanabilir.

def is_prime(num):
    """
    Alihan
    :param num:
    :return:
    """
    if num < 2:
        return False
    else:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
    return True


def karesi(n):
    return n * n


list1 = [1, 2, 4, 6, 7, 9, 4]

# listenin bir kopyasini cikarir:
list2 = [x for x in list1]
print(list2)

# listedeki her elemani +1 olan bi liste:
list2 = [x + 1 for x in list1]
print(list2)

# select
list3 = [x for x in list1 if x > 5]
print(list3)

# bu listeden cift sayilari alalim.
# bu listedeki cift sayilari iceren baska bir liste olusturalim.
list4 = [x for x in list1 if x % 2 == 0]
print(list4)

# listedeki asal sayilarin karelerini iceren bir list olusturalim.
list5 = [karesi(x) for x in list1 if is_prime(x)]
print(list5)

# set de ayni sekilde yapilabilir.

t1 = tuple((karesi(x) for x in list1 if is_prime(x)))
print(t1)
