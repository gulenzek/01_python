# Gun 02, listeler 2.py
from typing import List, Union

list1: list[Union[str, list[str]]] = ["batman", "in time", "inception", "wonderwoman", "flash"]

# slicing
# append
# stringler immutable
# list ise mutable
list1.append("aquaman") # none döndürürüm diyor.

s1 = "spiderman" # mutable, immutable
s1.upper()

# garbage collector (reference counting sistemi)

izlendi = None # null

sevdigim_film = "" # boş string

list1[3] = "back to the future"

list1[3] = ["back to the future", "back to the future 2"]



# Çok önemli birşey
# list1
list1[2:5] = ["back to the future", "back to the future 2"]

list1[1:4] = []


# listeye ekleme

list1 = list1 + ["merhaba"]
list1.count("a")
print(str(list1.count()))
print("done")


# Value Error z is not in list

list.pop(2)
list1.remove("a")


list2 = sorted(list1)
# sorted fonksiyonu var. dikkat..
print("done")


list1 = ["batman", "in time", "inception", "wonderwoman", "flash"]

# slicing
# append

list1.append("aquaman")  # aquman'i eklemis.
# list1: mutable

s1 = "spiderman" # 103
# string: immutable

s1 = s1.upper()  # SPIDERMAN 108
# SPIDERMAN

# garbage collector Java, .NET
# reference counting

s1 = "SPIDERMAN"
izlendi = None  # null

sevdigim_film = ""

list1[3] = "back to the future"
list1[3] = ["back to the future", "back to the future 2"]
# ['batman', 'in time', 'inception',
# ['back to the future', 'back to the future 2'], 'flash', 'aquaman']

# len()
list0 = ["batman", "in time", "inception", "wonderwoman", "flash", "aquaman"]
list1 = list0[:]  # copy
list1[2:5] = ["back to the future", "back to the future 2"]
# ['batman', 'in time', 'inception', 'wonderwoman', 'flash', 'aquaman']
# ['batman', 'in time', 'back to the future', 'back to the future 2', 'aquaman']

list1[1:4] = []
# ['batman', 'aquaman']


list4 = ["batman", "aquaman"]
list5 = list4.copy()  # [:] yazsak da olurdu.
list5.append("wonderwoman")


s1 = "abc"
s2 = s1
id1 = id(s1)
id2 = id(s2)
s2 = s2 + "d"
id2 = id(s2)

list4 = ["batman", "aquaman"]
id4 = id(list4)
list4 = list4 + ["wonderwoman"]
id5 = id(list4)

list6 = ["a", "b", "a", "d", "c"]
kac_tane = list6.count("a")

# list6.clear()
list6.extend(["x", "y", "z"])

list6.copy()
kacinci = list6.index("c")

# kacinci = list6.index("Z")
# (<class 'ValueError'>, ValueError("'Z' is not in list"), <traceback object at 0x0000016B50B51340>)

list6.insert(2, "Q")

print("done")

#----------------------------------

list1 = ["batman", "in time", "inception", "wonderwoman", "flash"]

# slicing
# append

list1.append("aquaman")  # aquman'i eklemis.
# list1: mutable

s1 = "spiderman" # 103
# string: immutable

s1 = s1.upper()  # SPIDERMAN 108
# SPIDERMAN

# garbage collector Java, .NET
# reference counting

s1 = "SPIDERMAN"
izlendi = None  # null

sevdigim_film = ""

list1[3] = "back to the future"
list1[3] = ["back to the future", "back to the future 2"]
# ['batman', 'in time', 'inception',
# ['back to the future', 'back to the future 2'], 'flash', 'aquaman']

# len()
list0 = ["batman", "in time", "inception", "wonderwoman", "flash", "aquaman"]
list1 = list0[:]  # copy
list1[2:5] = ["back to the future", "back to the future 2"]
# ['batman', 'in time', 'inception', 'wonderwoman', 'flash', 'aquaman']
# ['batman', 'in time', 'back to the future', 'back to the future 2', 'aquaman']

list1[1:4] = []
# ['batman', 'aquaman']


list4 = ["batman", "aquaman"]
list5 = list4.copy()  # [:] yazsak da olurdu.
list5.append("wonderwoman")


s1 = "abc"
s2 = s1
id1 = id(s1)
id2 = id(s2)
s2 = s2 + "d"
id2 = id(s2)

list4 = ["batman", "aquaman"]
id4 = id(list4)
list4 = list4 + ["wonderwoman"]
id5 = id(list4)

list6 = ["a", "b", "a", "d", "c"]
kac_tane = list6.count("a")

# list6.clear()
list6.extend(["x", "y", "z"])

list6.copy()
kacinci = list6.index("c")

# kacinci = list6.index("Z")
# (<class 'ValueError'>, ValueError("'Z' is not in list"), <traceback object at 0x0000016B50B51340>)

list6.insert(2, "Q")

list7 = list6.copy()
eleman = list7.pop(2)
eleman2 = list7.pop()
list7.pop()

list7.remove("a")
# bulamazsa: ValueError

list7.reverse()

list7.sort()
list8 = sorted(list7)

print("done")
