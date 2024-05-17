def remove_repeated_elements(arr):
    return set(arr)


def remove_repeated_elements2(arr):
    map1 = {}
    for a in arr:
        if not map1.get(a):
            map1.update({a: 1})
    return map1.keys()

def remove_repeated_elements3(arr):
    lst = []
    for a in arr:
        if a not in lst:
            lst.append(a)
    return lst        


print(remove_repeated_elements3(['python', 'java', 'c', 'c#', 'java', 'ruby', 'c']))
