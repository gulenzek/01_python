# map1.py

def middlestrip3(lakirti):
    """
    Q1
    @author: Zeki Gülen, 17/10/2020

    terim = "            a b  "
    terim1 = "  A \n  a d@  1  2 \t"
    terim2 = "   aa b c   "

    print(middlestrip3(terim))
    print(middlestrip3(terim1))
    print(middlestrip3(terim2))
    """
    return (len(lakirti) - len(lakirti.lstrip())) * " " + "".join(lakirti.split()) + (
            len(lakirti) - len(lakirti.rstrip())) * " "

list1 = ["tahta kurusu", "  tahta  kurusu", "erik çekirdeği", "  üzümün sapı"]

# bu listenin her elemanini, middlestrip3 fonksiyonundan gecirmek istersek.
list2 = []
for item in list1:
    result = middlestrip3(item)
    list2.append(result)
print(list2)

# idiom

list3 = list(map(middlestrip3, list1))
print(list3)

