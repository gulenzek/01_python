# -*- coding: utf-8 -*-
"""
pickle_class_load_save.py
"""

import pickle

class AkilliTelefon:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def __str__(self):
        return f"{self.marka} {self.model}"

    def __repr__(self):
        return str(self)


def pickle_save(file_name):
    iphone12 = AkilliTelefon("Apple", "iPhone 12")
    samsungs9 = AkilliTelefon("Samsung", "S9")
    telefonlar = [iphone12, samsungs9]
    handle = open(file_name, "wb")
    pickle.dump(telefonlar, handle)
    handle.close()


def pickle_load(file_name):
    handle = open(file_name, "rb")
    son_cikan_telefon = pickle.load(handle)
    handle.close()
    print(son_cikan_telefon)

def main():
    file_name = "telefon_data.pickle"
    pickle_save(file_name)
    pickle_load(file_name)


if __name__ == "__main__":
    main()
