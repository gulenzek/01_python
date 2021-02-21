# -*- coding: utf-8 -*-
"""
pickle_load1.py
"""

import pickle

def main():
    handle = open("renk_verisi.pickle", "rb")
    data = pickle.load(handle)
    handle.close()
    print(data)

if __name__ == "__main__":
    main()
