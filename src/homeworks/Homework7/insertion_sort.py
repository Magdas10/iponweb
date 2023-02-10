def insertion_sort(lst: list):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j = j - 1


lst1 = [1, 7, 9, 32, 6, 890, 765]
insertion_sort(lst1)
print(lst1)
lst2 = [90, 80, 70, 60]
insertion_sort(lst2)
print(lst2)
lst3 = [90, 100, 2, 3]
insertion_sort(lst3)
print(lst3)
lst4 = [1, 2, 3, 4]
insertion_sort(lst4)
print(lst4)
