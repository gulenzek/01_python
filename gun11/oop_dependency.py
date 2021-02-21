# -*- coding: utf-8 -*-
"""
oop_dependency.py
"""

class Database:
    pass


class BankAccount:
    def save_to_database(self, db1):
        # db1 = Database()
        db1.ip = "192.dsfgg"
        db1.pwd = "Dfgdfg"

        # database connection
        pass

def main():
    db1 = Database()
    ba1 = BankAccount()
    ba1.save_to_database(db1)
    # Spring


if __name__ == "__main__":
    main()
