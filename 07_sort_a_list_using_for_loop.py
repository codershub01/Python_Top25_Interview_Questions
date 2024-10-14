## Sorting a list using for loop

def sort_list(lst):
    print("Given list :", lst)
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>=lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print("Sorted list :", lst)

sort_list([65,98,23,55,2,4,61,87,49])