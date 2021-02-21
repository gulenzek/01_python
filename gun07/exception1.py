# TRY ve EXCEPT olayını öğreniyoruz..

def get_a_number():
    while True:
        try:
            number = float(input(">>>"))
            break # Bu satıra ulaşmışsa exception yoktur.
            file = open("olmayan_dosya.txt", "r")
            file.close()

        except ValueError:
            print("Girdiğiniz değer float değildir!")
            # ??? Burada kırmak yok!
    return number

number2 = get_a_number()


def prim_hesapla(data):
    # hata yükseltmek - hata fırlatmak
    raise NotImplementedError

def is_prime(number1):
    assert isinstance(number1, int)
    if number1 <= 0:
        raise ValueError("Verdiğiniz sayı pozitif olmalıdır!")
    # TODO: işlemleri yap.


    # index = ValueError
    # find = -1 döndürürüm diyor.
    