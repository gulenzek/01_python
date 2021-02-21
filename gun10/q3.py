# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
q3 tokenize()
bir string'i kelimelere ayiran, aşağıdaki fonksiyonu yazınız.
def tokenize(haystack: str, min_allowed_length=3):
    Tokenizes a string.

    str1 = r"\tech\Python\ML, AI\Kaggle\Relationship_between_Earthquakes_and_Solar_System"
    tokens = tokenize(str1)
    print(tokens)

    ['tech', 'Python', 'ML', 'AI', 'Kaggle', 'Relationship', 'between', 'Earthquakes', 'and', 'Solar', 'System']

    :param min_allowed_length: only the words longer than this is accepted, others are ignored.
    :param haystack: string to tokenize
    :return: tokens as list of strings.

"""
import nltk


def tokenize(haystack: str, min_allowed_length=3):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    token = tokenizer.tokenize(haystack)
    yeni = []
    for i in token:
        if len(i) >= min_allowed_length:
            yeni.append(i)
    return yeni


# str1 = r"Merhaba dünya. Merhaba dünyalı arkadaş. Kahve içer misin? Havalar soğuk"

str1 = r"\tech\Python\ML, AI\Kaggle\Relationship_between_Earthquakes_and_Solar_System"

print(tokenize(str1))
