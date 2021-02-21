# -*- coding: utf-8 -*-
"""
oop1.py
https://www.python-course.eu/python3_magic_methods.php
operator overloading
"""

class BankAccount:
    def __init__(self, balance=0):
        assert isinstance(balance, (float, int))

        if balance < 0:
            raise ValueError("Balance must be zero or positive")

        if balance > 0:
            self.__balance = balance
            self.__account_activities = [balance]

    @property
    def balance(self):
        return self.__balance

    @property
    def account_activities(self):
        return self.__account_activities

    def withdraw(self, amount):
        self.__check_amount(amount)

        if amount > self.balance:
            print("Insufficient balance")
            return
        elif amount == 0:
            return

        self.__balance -= amount
        self.__account_activities.append(-amount)

    def __check_amount(self, amount):
        assert isinstance(amount, (float, int))
        if amount < 0:
            raise ValueError("Amount must be zero or positive")
        return

    def deposit(self, amount):
        self.__check_amount(amount)
        if amount == 0:
            return

        self.__balance += amount
        self.__account_activities.append(amount)

    def __add__(self, other):
        # ba1 + ba2
        # self + other
        self.__balance = self.__balance + other.balance
        # other.__balance -= other.__balance
        other.withdraw(other.balance)
        return self

    def __gt__(self, other):
        #      ba1     ba2
        if self.__balance > other.__balance:
            return True
        return False

    def __str__(self):
        return "balance: " + str(self.balance)

def main():
    ba1 = BankAccount(100)
    ba2 = BankAccount(200)
    ba1 = ba1 + ba2
    print(ba1)  # 300
    print(ba2)  # 0

    if ba1 > ba2:
        # TypeError: '>' not supported between instances of 'BankAccount' and 'BankAccount'
        print("buyuk")
    else:
        print("buyuk degil")

if __name__ == "__main__":
    main()
