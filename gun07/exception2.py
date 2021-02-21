import datetime

def is_prime(number1):
    """
    AssertionError, ValueError
    :param number1:
    :return:
    """
    assert isinstance(number1, int)
    if number1 <= 0:
        raise ValueError("verdiginiz sayi pozitif olmalidir.")
    # TODO: islemleri yap
    return None

try:
    value1 = -2  # bunun kullanicidan geldigini dusunelim.
    value2 = is_prime(value1)
except ValueError as err1:
    log_str = "verilen sayi: {} hata: {}".format(value1, err1)
    # loglayabiliriz: verilen hatayı loglayabiliriz. as kullanmak gerekiyor.
    print(log_str)




def is_valid_date(year, month, day):
    """

    :param year:
    :param month:
    :param day:
    :return:
    """
    datetime.datetime(2015, 2, 3)

is_valid_date(None, None, None)

import datetime

def is_prime(number1):
    """
    AssertionError, ValueError
    :param number1:
    :return:
    """
    assert isinstance(number1, int)
    if number1 <= 0:
        raise ValueError("verdiginiz sayi pozitif olmalidir.")
    # TODO: islemleri yap
    return None

try:
    value1 = -2  # bunun kullanicidan geldigini dusunelim.
    value2 = is_prime(value1)
except ValueError as err1:
    log_str = "verilen sayi: {} hata: {}".format(value1, err1)
    # loglayabiliriz:
    print(log_str)

def is_valid_date(year, month, day):
    """
    import datetime
    """
    try:
        datetime.datetime(year, month, day)
        result = True  # bu satira ulasabildiyse
    except ValueError:
        result = False
    return result

print(is_valid_date(2020, 10, 22))  # T
print(is_valid_date(2020, 10, 32))  # F
# bizim fonksiyonumuz, string parametre alabilse de,
# Python'un datetime.datetime() fonksiyonu int bekliyor.
# print(is_valid_date("2020", "10", "32"))  # TypeError


try:
except:
finally:
    # bir kez yazılıyor. connectionlarda yazılabiliyor. connection kapanması vesair ile ilgili.