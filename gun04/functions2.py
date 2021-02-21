# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
 Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a
 hyphen-separated sequence after sorting them alphabetically.
"""

# texts = [n for n in input(">>>").split(' ')]
# print(texts)
# texts.sort()
# print(texts)
# print('-'.join(texts))
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


thislist = ["apple", "banana", "cherry"]

# if "apple" in thislist:
#     print("Yes, '[]' is in the fruits list")
#
# for n in range(21, 0, -3):
#     print(n, end="\n")


# for i in range(1, 100): # burada döngü değişkeni olarak i kullanılmıştır.
#     print(i, i-1)


print(thislist)
third_list = thislist
second_list = thislist.copy()

print(second_list)
print(id(thislist))
print(id(third_list))
print(id(second_list))