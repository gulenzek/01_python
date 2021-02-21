# -*- coding: utf-8 -*-
"""
- [ ] En çok gol atan takım
- [ ] En az gol yiyen takım
- [ ] En farklı skorla biten 10 maç
- [ ] En çok gol atılan 10 maç
- [ ] En çok maç oynanmış şehir
- [ ] En çok maç oynanmış ülke
- [ ] En Uzun Yenilmezlik ünvanı
- [ ] Her bir turnuvadaki mac sayısı
"""

import csv

def main():
    file_name = "results.csv"
    with open(file_name, "r", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            city = row[1]
            print(city)


if __name__ == "__main__":
    main()
