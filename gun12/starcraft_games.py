# -*- coding: utf-8 -*-
"""
starcraft_games.py
"""


def get_raw_data():
    data = """
    Game 	GameRankings 	Metacritic
    StarCraft 	(PC) 93%[109] 	(PC) 88[111]
    Insurrection 	48%[113] 	—
    Retribution 	—[114] 	—
    StarCraft: Brood War 	95%[115] 	—
    StarCraft II: Wings of Liberty 	92%[116] 	93[117]
    StarCraft II: Heart of the Swarm 	86%[118] 	86[119]
    StarCraft II: Legacy of the Void 	88%[120] 	88[121]
    """
    return data


def split_to_lines(raw_data):
    return raw_data.strip().splitlines()


def extract_point(text):
    """
    >>> extract_point("(PC) 93%[109] -> 109")
    109
    >>> extract_point("(PC) 88[111] -> 111")
    111
    >>> extract_point("'—'")
    None
    :return:
    """
    # TODO: extract_point()
    pass


def parse_data(lines):
    header_line = lines.pop(0)
    parsed_elements = []
    for line in lines:
        parts = line.split("\t")
        parts = [x.strip() for x in parts]
        print(parts)
        # ['StarCraft II: Legacy of the Void', '88%[120]', '88[121]']
        # TODO: parts'in ilgili elemanlarini extract_point()'den gecirelim.
        # TODO: bu elemanlari kullanarak bir dict olusturalim.
        # TODO: bu dict'i bir list'e ekleyelim.
    print(parsed_elements)
    # TODO: list'i dondurelim.


def main():
    raw_data = get_raw_data()
    lines = split_to_lines(raw_data)
    parsed_lines = parse_data(lines)
    # [
    # {"game":"StarCraft", "GameRankings":109, "Metacritic":111}
    # ...
    # ]
    print()


if __name__ == "__main__":
    main()
