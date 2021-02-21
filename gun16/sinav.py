def except_letters(text: str, unwanted_letters: str):
    # TODO: cevabınızı buraya yazınız.
    result = ""
    letters_list, unwanted_letters_list = [], []
    for harf in text:
        if harf not in unwanted_letters:
            letters_list += harf

    return letters_list


print(except_letters("liverpool", "o"))
print(except_letters("deneme", "en"))

# actual1 = except_letters("Liverpool", "o")
# assert actual1 == "Liverpl"
#
# actual1 = except_letters("deneme", "en")
# assert actual1 == "dm"
#
# actual1 = except_letters("deneme", "xy")
# assert actual1 == "deneme"
