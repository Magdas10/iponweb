
def counting_sort(lst: list):
    size = len(lst)
    result = [0] * size
    count = [0] * 10

    for i in range(size):
        count[lst[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        result[count[lst[i]] - 1] = lst[i]
        count[lst[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        lst[i] = result[i]


lst1 = [9, 4, 2, 2, 8, 3, 3, 1]
counting_sort(lst1)
print(lst1)

lst2 = [2, 3, 1, 5, 7]
counting_sort(lst2)
print(lst2)
