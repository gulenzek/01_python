# -*- coding: utf-8 -*-
"""

"""

import json

def json_load():
    renkler = {}
    renkler["kirmizi"] = ("kirmizi", 1)
    renkler["yesil"] = ("green", 2)
    renkler["siyah"] = "undefined"

    # dict -> json, serialize
    # Serialize obj to a JSON formatted str.
    json1 = json.dumps(renkler)
    assert isinstance(json1, str)
    print(json1)

    handle = open("json_data.json", "wt", encoding="utf8")
    json.dump(renkler, handle)
    handle.close()

    # json str -> python obj, deserialize
    renkler2 = json.loads(json1)

    # deney:
    # renkler2 = json.loads(json1 + "}")
    # json.decoder.JSONDecodeError: Extra data: line 1 column 73 (char 72)
    print()

    handle2 = open("json_data.json", "rt", encoding="utf8")
    renkler3 = json.load(handle2)
    handle2.close()
    print(renkler3)


def main():
    json_load()


if __name__ == "__main__":
    main()
