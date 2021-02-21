def get_a_number():
    while True:
        try:
            number = input(">>>")
            number = float(number)
            file = open("olmayan_dosya.txt", "r")
            file.close()
            break  # bu satira ulasmis ise, exception yoktur.
        except Exception:
            print("kesin kotu birseyler oluyor.")
    return number

# number2 = get_a_number()

def maaslar_hesapla(file_name):
    handle = open(file_name, "r")
    # islemleri yap.
    handle.close()

def prim_hesapla(data):
    # hata yukseltmek = hata firlatmak
    raise NotImplementedError("prim_hesapla() fonksiyonu henuz bitirilmedi.")

def bordro_hesapla(data):
    # ne gerekiyorsa onu yazar.
    pass

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

def main():
    prim_hesapla(None)
    maaslar_hesapla("dosya.txt")
    s1 = ""
    s1.index()

# boyle yapmayalim:
# try:
#     main()
# except Exception:
#     print("bu dosya yok:", file_name)
#     print("bir hata olustu")

main()
