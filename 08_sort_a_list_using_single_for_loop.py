## Sorting a list using a single for loop

def sort_list(lst):
    n = len(lst) - 1
    print("Given list :", lst)
    for i in range(n*n):
        p = i % n
        if lst[p] >= lst[p+1]:
            lst[p], lst[p+1] = lst[p+1], lst[p]

    print("Sorted List :", lst)

sort_list([65,98,23,55,2,4,61,87,49])