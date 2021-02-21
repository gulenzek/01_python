a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:  # set icinde var mi diye kontrol ediyor.
        uniq_items.append(x)
        dup_items.add(x)  # set'e ekliyor.

print(uniq_items)  # list
print(dup_items)  # set


# ___________

list1 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
listu = []
for item in list1:
    if item not in listu:  # O(n)
        listu.append(item)
