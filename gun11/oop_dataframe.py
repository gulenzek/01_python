# -*- coding: utf-8 -*-
"""
oop_dataframe.py
"""

import pandas as pd

# DataFrame

def main():
    df1 = pd.read_excel("yemek_tarifleri.xlsx")
    df2 = df1[["tarif_adi", "tuz_miktari"]]  # DataFrame
    series1 = df1["tarif_adi"]  # Series
    print()


if __name__ == "__main__":
    main()
