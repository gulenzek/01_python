# q = m, c, t1, t2

def q(m: float, c: float, t1: float, t2: float):
    return m * c * (t2 - t1)


# ortalama hesabı list

def ortalama(list1):
    kac_tane = len(list1)
    toplam = sum(list1)
    ortala = toplam/kac_tane
    return ortala


import random


def is_palindrome(word):
    # word = "xaaZax"
    isPalindrome = True
    for i in range(0, len(word) // 2):
        soldan = word[i]
        sagdan = word[((len(word) - 1) - i)]
        if soldan != sagdan:
            # if word[i] != word[((len(word) - 1) - i)]:
            isPalindrome = False
            break
    return isPalindrome


def factorial(n):
    """
    factorial hesabi yapar.

    :param n: n sayisi
    :return: factorial degeri
    """
    toplam = 1
    for i in range(n, 0, -1):
        toplam = toplam * i
        # print(i)
    return toplam


def generate_numbers(kac_tane):
    numbers = []
    while True:
        number1 = random.randint(1, 100)
        if number1 not in numbers:
            numbers.append(number1)
        if len(numbers) == kac_tane:
            break
    return numbers


def generate_numbers2(kac_tane, kactan=1, kaca=100):
    numbers = []
    while True:
        number1 = random.randint(kactan, kaca)
        if number1 not in numbers:
            numbers.append(number1)
        if len(numbers) == kac_tane:
            break
    return numbers

def isi_hesabi(m, c, t1, t2):
    # q = m*c*dt
    # fonksiyoun adi q olsun.
    # m, c, t1, t2
    a = m * c * abs(t2 - t1)
    return a


def avg(list1):
    kac_tane = len(list1)
    toplam = sum(list1)
    ortalama = toplam / kac_tane
    return ortalama


def avg_no_peak(list1):
    list1.sort()
    list1.pop()
    list1.pop(0)
    ortalama = avg(list1)
    return ortalama


def main():
    # data = read_data()
    # hata_var_mi = validate_data(data)
    # data2 = calculate_data(data)
    # send_mail(data2)
    # save_to_database(data2)

    numbers = generate_numbers2(5, 1, 100)
    print(generate_numbers2(5, 1, 100))  # explicit
    print(generate_numbers2(5))
    print(generate_numbers2(5, 2, 10))

    number1 = 3
    toplam = 39

    # print(is_palindrome("1221"))  # T
    # print(is_palindrome("12321"))  # T
    # print(is_palindrome("44322"))  # F
    #
    # print(factorial(100))  # .........
    # print(factorial(5))  # 120
    # print(factorial(2))  # 2
    # print(factorial(1))  # 1
    # print(factorial(0))  # 1

    q = isi_hesabi(100, 2, 100, 5)
    print(q)

    ortalama = avg([10, 20, 30])
    print(ortalama)

    ortalama = avg_no_peak([1, 10, 20, 30, 31])
    print(ortalama)

# best programming practice
main()

import random


def is_palindrome(word):
    # word = "xaaZax"
    isPalindrome = True
    for i in range(0, len(word) // 2):
        soldan = word[i]
        sagdan = word[((len(word) - 1) - i)]
        if soldan != sagdan:
            # if word[i] != word[((len(word) - 1) - i)]:
            isPalindrome = False
            break
    return isPalindrome


def factorial(n):
    """
    factorial hesabi yapar.

    :param n: n sayisi
    :return: factorial degeri
    """
    toplam = 1
    for i in range(n, 0, -1):
        toplam = toplam * i
        # print(i)
    return toplam


def generate_numbers(kac_tane):
    numbers = []
    while True:
        number1 = random.randint(1, 100)
        if number1 not in numbers:
            numbers.append(number1)
        if len(numbers) == kac_tane:
            break
    return numbers


def generate_numbers2(kac_tane, kactan=1, kaca=100):
    numbers = []
    while True:
        number1 = random.randint(kactan, kaca)
        if number1 not in numbers:
            numbers.append(number1)
        if len(numbers) == kac_tane:
            break
    return numbers

def isi_hesabi(m, c, t1, t2):
    # q = m*c*dt
    # fonksiyoun adi q olsun.
    # m, c, t1, t2
    a = m * c * abs(t2 - t1)
    return a


def avg(list1):
    kac_tane = len(list1)
    toplam = sum(list1)
    ortalama = toplam / kac_tane
    return ortalama


def avg_no_peak(list3):
    # list, mutable bir tiptir.
    # bu fonksiyonun, disaridaki nesneye etki etmemesi icin,
    # kopyasi uzerinde calisalim:
    # bu da olabilirdi:
    # list1 = sorted(list2)
    list1 = list3[:]
    list1.sort()
    list1.pop()  # son elemanini siler.
    list1.pop(0)
    ortalama = avg(list1)
    return ortalama


# Bir sayıya kadar olan sayıların toplamını döndüren bir fonksiyon yazınız.
def sum_up_to(number):
    pass


def histogram_ciz(word):
    """
    Bir str'nin harflerinden kac tane oldugunu gosteren bir grafik cizer.
    histogram_ciz("batman")

    b 1 #
    a 2 ##
    t 1 #
    m 1 #
    n 1 #

    :param word: "batman" gibi bir kelime
    :return: None
    """
    harfler = {}
    for harf in word:
        # print(harf)
        harfler[harf] = harfler.get(harf, 0) + 1

    karakter = "_"
    for harf in harfler:
        print(harf, harfler.get(harf), harfler.get(harf) * karakter)

    print()

histogram_ciz("batman")

def main():
    # data = read_data()
    # hata_var_mi = validate_data(data)
    # data2 = calculate_data(data)
    # send_mail(data2)
    # save_to_database(data2)

    numbers = generate_numbers2(5, 1, 100)
    print(generate_numbers2(5, 1, 100))  # explicit
    print(generate_numbers2(5))
    print(generate_numbers2(5, 2, 10))

    number1 = 3
    toplam = 39

    # print(is_palindrome("1221"))  # T
    # print(is_palindrome("12321"))  # T
    # print(is_palindrome("44322"))  # F
    #
    # print(factorial(100))  # .........
    # print(factorial(5))  # 120
    # print(factorial(2))  # 2
    # print(factorial(1))  # 1
    # print(factorial(0))  # 1

    q = isi_hesabi(100, 2, 100, 5)
    print(q)

    ortalama = avg([10, 20, 30])
    print(ortalama)

    list2 = [1, 10, 20, 30, 31]
    ortalama = avg_no_peak(list2)
    print(list2)
    print(ortalama)

# best programming practice
# main()

