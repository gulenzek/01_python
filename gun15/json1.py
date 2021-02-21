# -*- coding: utf-8 -*-
"""
json1.py
"""

import json

data_str = """
{
	"name": "Luke Skywalker",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"skin_color": "fair",
	"eye_color": "blue",
	"birth_year": "19BBY",
	"gender": "male",
	"homeworld": "https://swapi.dev/api/planets/1/",
	"films": [
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/6/",
		"https://swapi.dev/api/films/3/",
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/7/"
	],
	"species": [
		"https://swapi.dev/api/species/1/"
	],
	"vehicles": [
		"https://swapi.dev/api/vehicles/14/",
		"https://swapi.dev/api/vehicles/30/"
	],
	"starships": [
		"https://swapi.dev/api/starships/12/",
		"https://swapi.dev/api/starships/22/"
	],
	"created": "2014-12-09T13:50:51.644000Z",
	"edited": "2014-12-20T21:17:56.891000Z",
	"url": "https://swapi.dev/api/people/1/"
}"""


def main():
    x = json.loads(data_str)  # load string
    print()


if __name__ == "__main__":
    main()


def main():
    data = json.loads(data_str)  # load string
    print()

    renkler = {}
    renkler["kirmizi"] = ["red", "crimson"]
    renkler["siyah"] = ["black", "dark"]
    renkler["turuncu"] = "orange"

    # sort_keys=True, indent=4
    json_str = json.dumps(renkler, indent=4)  # dump string
    print(json_str)

    handle = open("data1.json", "w", encoding="utf8")
    handle.write(json_str)
    handle.close()

    str1 = """
    {"time":{"updated":"Nov 5, 2020 12:39:00 UTC","updatedISO":"2020-11-05T12:39:00+00:00","updateduk":"Nov 5, 2020 at 12:39 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"14,828.8123","description":"United States Dollar","rate_float":14828.8123},"GBP":{"code":"GBP","symbol":"&pound;","rate":"11,345.7912","description":"British Pound Sterling","rate_float":11345.7912},"EUR":{"code":"EUR","symbol":"&euro;","rate":"12,556.1930","description":"Euro","rate_float":12556.193}}}
    """


if __name__ == "__main__":
    main()
