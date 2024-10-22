## Get smallest value from list

## Solution : 1
def get_max(lst):
    lst.sort()
    return lst[0]

print(get_max([23,54,65,98,27,45,16,83]))


## Solution : 2
def get_max(lst):
    x = lst[0]

    for i in lst:
        if i<x:
            x=i

    return x
print(get_max([23,54,65,98,27,45,16,83]))
