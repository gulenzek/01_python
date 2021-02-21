# list_comprehension2.py

# Adil, list comprehensions.
examplestring = " Ali    ,    calis    ,     kazan"
words = examplestring.split(",")

# wordtrimFunction = lambda a: a.strip()
def wordtrimFunction(a):
    return a.strip()

# map(function, iterable)
wordsWithoutSpaces = map(wordtrimFunction, words)
result = " ".join(wordsWithoutSpaces)
print(result)

list1 = [wordtrimFunction(word) for word in words]

print(list1)


# list_comprehension2.py

# wordtrimFunction = lambda a: a.strip()
def wordtrimFunction(a):
    return a.strip()

# Adil, list comprehensions.
examplestring = " Ali    ,    calis    ,     kazan"
words = examplestring.split(",")

words2 = [x for x in words]
words3 = [wordtrimFunction(x) for x in words]
words4 = [x.strip() for x in words]
words5 = [print(x.strip(), "___") for x in words]

# yukaridaki kod, map() fonksiyonunun kullanimina bir alternatif olusturuyor:
# map(function, iterable)
# wordsWithoutSpaces = map(wordtrimFunction, words)
# result = " ".join(wordsWithoutSpaces)
# print(result)

customers = ["Alice", "Bob", "Frank", "Ann"]

list2 = [x for x in customers if x.startswith("A")]

print(list2)
a