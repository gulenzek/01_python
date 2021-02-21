# -*- coding: utf-8 -*-
"""
pickle etmek: tursulamak, serialize etmek, diske yaziyor.
unpickle: deserialize etmek, diskten okumak

i7, 16GB RAM, 2.5 saat, model olusturma.

model_2020-11-06_03-15.pickle
model_2020-11-07_03-18.pickle

audi a8: 420.000 TL
audi a8: 120.000 TL
  aigr hasarlidir. amcaoglu guzelce topladi.
"""

import collections
import pickle

def read_binary():
    file_name = "Applied Data Science Techniques with Using Python.pdf"
    handle = open(file_name, "rb")
    data = handle.read()
    handle.close()
    print()

def main():
    # namedtupe'i pickle edemedi:
    # Renk = collections.namedtuple("Renk", ["ingilizce", "renk_kodu"])

    renkler = {}
    renkler["kirmizi"] = ("kirmizi", 1)
    renkler["yesil"] = ("green", 2)
    renkler["siyah"] = "undefined"
    # bu noktada
    handle = open("renk_verisi.pickle", "wb")
    pickle.dump(renkler, handle)

    # dumps, dump string gibi, ama aslinda bytes'a ceviriyor.
    # byte_obj = pickle.dumps(renkler)

    handle.close()

    read_binary()

    print(pickle.HIGHEST_PROTOCOL)  # 5
    print()



if __name__ == "__main__":
    main()
