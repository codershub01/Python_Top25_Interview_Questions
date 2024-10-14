## Sorting a nested list based on second element of sublist

def sort_nested_list(lst):
    print("Given list :",lst)
    for i in range(0, len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j][1]> lst[j+1][1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print("Sorted list :", lst)

sort_nested_list([['Mango', 10], ['Cucumber', 5], ['Apple', 20], ['Rose', 15]])