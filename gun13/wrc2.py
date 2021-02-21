# -*- coding: utf-8 -*-
"""
wrc1.py

en cok sampiyon olan 5 driver
en cok sampiyon olan 5 takim(manufacturer)
en cok sampiyon olan 5 araba
pespese en cok sampiyon olan driver
pespese en cok sampiyon olan takim
"""

import collections
import csv
import pprint


def read_data(file_name):
    with open(file_name, "r", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        lines = collections.deque()
        for row in reader:
            lines.append(row)

        # ilk 2 satiri drop edelim:
        # deque kullansak daha hizli calisir:
        lines.popleft()
        lines.popleft()
    return lines


def en_cok_sampiyon_olanlar(lines, sampiyonluk=5):
    result_drivers = {}
    result_manufacturers = {}
    for line in lines:
        season = line[0]
        driver = line[1]
        driver_car = line[2]
        manufacturer = line[3]
        manufacturer_car = line[4]

        if driver != "No drivers' championship[f]":
            result_drivers[driver] = result_drivers.get(driver, 0) + 1

        # if driver in result:
        #     result[driver] += 1
        # else:
        #     result[driver] = 1
        result_manufacturers[manufacturer] = result_manufacturers.get(manufacturer, 0) + 1

    result_drivers = sorted(result_drivers.items(), key=lambda x: x[1], reverse=True)[:sampiyonluk]
    result_manufacturers = sorted(result_manufacturers.items(), key=lambda x: x[1], reverse=True)[:sampiyonluk]
    return result_drivers, result_manufacturers


def en_cok_sampiyon_olan_drivers(lines, sampiyonluk=5):
    result_drivers, result_manufacturers = en_cok_sampiyon_olanlar(lines, sampiyonluk)
    return result_drivers


def en_cok_sampiyon_olan_manufacturers(lines, sampiyonluk=5):
    result_drivers, result_manufacturers = en_cok_sampiyon_olanlar(lines, sampiyonluk)
    return result_manufacturers


class Championship:
    def __init__(self, season, driver, driver_car, manufacturer, manufacturer_car):
        self.season = season
        self.driver = driver
        self.driver_car = driver_car
        self.manufacturer = manufacturer
        self.manufacturer_car = manufacturer_car
        self._fix_driver_car_name()

    def _fix_driver_car_name(self):
        self.manufacturer_car = self.manufacturer_car.replace("06/07", "06")
        self.manufacturer_car = self.manufacturer_car.replace("Integrale 16V", "Integrale")
        self.manufacturer_car = self.manufacturer_car.replace("Impreza WRC", "Impreza 555")
        self.manufacturer_car = self.manufacturer_car.replace("205 Turbo 16 E2", "205 Turbo 16")

    def __repr__(self):
        result = ""
        result += self.season + "|"
        result += self.driver + "|"
        result += self.driver_car + "|"
        result += self.manufacturer + "|"
        result += self.manufacturer_car + "  "
        return result


def en_cok_sampiyon_olan_araba(lines, sampiyonluk=5):
    championships = []
    en_cok_sampiyon_olan_arabalar = {}
    for line in lines:
        season = line[0]
        driver = line[1]
        driver_car = line[2]
        manufacturer = line[3]
        manufacturer_car = line[4]
        ch1 = Championship(season, driver, driver_car, manufacturer, manufacturer_car)
        championships.append(ch1)
        en_cok_sampiyon_olan_arabalar[ch1.manufacturer_car] = en_cok_sampiyon_olan_arabalar.get(ch1.manufacturer_car, 0) + 1

    en_cok_sampiyon_olan_arabalar2 = sorted(en_cok_sampiyon_olan_arabalar.items(), key=lambda x : x[1], reverse=True)

    pp1 = pprint.PrettyPrinter()
    pp1.pprint(championships)


def main():
    lines = read_data("WRC.csv")
    result_drivers, result_manufacturers = en_cok_sampiyon_olanlar(lines)
    assert isinstance(lines[1], list)
    print(lines)
    en_cok_sampiyon_olan_araba(lines)


if __name__ == "__main__":
    main()
