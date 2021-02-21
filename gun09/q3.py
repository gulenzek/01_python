# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
Kesir sadeleştirme problemi. (Tam sayı olarak)
"""
i = 2
pay = int(input("Pay >>>"))
payda = int(input("Payda >>>"))
kesir = str(pay) + "/" + str(payda)
kucuk = min(pay, payda)
while i <= kucuk:
    if pay % i == 0 and payda %i == 0:
        pay /= i
        payda /= i
        kucuk /= i
        i = 2
    else:
        i += 1
print("{} kesrinin sadeleştirilmiş hali {}/{} olur.".format(kesir, int(pay), int(payda)))
def main():
    pass


if __name__ == "__main__":
    main()
