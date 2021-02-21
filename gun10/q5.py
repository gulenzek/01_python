# -*- --coding:utf-8 -*-
# @author: gulenzek
"""
q5 reverse_lookup()
Write a function named reverse_lookup that finds all of the keys in a dictionary that map to a specific value.
The function will take the dictionary and the value to search for as its only parameters. It will return a
(possibly empty) list of keys from the dictionary that map to the provided value.

Include a main program that demonstrates the reverseLookup function as part of your solution to this exercise.
Your program should create a dictionary and then show that the reverseLookup function works correctly when it
returns multiple keys, a single key, and no keys. Ensure that your main program only runs when the file containing
your solution to this exercise has not been imported into another program.

"""


def reverse_lookup(dict):
    lookup_value = 2
    all_keys = []
    for key, value in dict.items():
        if value == lookup_value:
            all_keys.append(key)
    return all_keys


print(reverse_lookup({'ankara': 1, 'bursa': 16, 'istanbul': 2, 'diyarbakır': 22}))
