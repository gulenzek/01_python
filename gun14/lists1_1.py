def last(n): return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last([(1,5), (1,9),(7,2)]))