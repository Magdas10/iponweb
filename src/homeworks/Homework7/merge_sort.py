import numpy


def merge(first: list, second: list):
    merged_array = list()
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        merged_array.append(first.pop(i) if first[i] < second[j] else second.pop(j))
    merged_array.extend(first)
    merged_array.extend(second)
    return merged_array


def sorting(lst: list):
    half_of_array = len(lst) // 2
    if len(lst) < 2:
        return lst
    return merge(sorting(lst[0:half_of_array]), sorting(lst[half_of_array:len(lst)]))


lst1 = [1, 7, 9, 32, 6, 890, 765]
print(sorting(lst1))
lst2 = [90, 80, 70, 60]
print(sorting(lst2))
lst3 = [90, 100, 2, 3]
print(sorting(lst3))
lst4 = [1, 2, 3, 4]
print(sorting(lst4))
