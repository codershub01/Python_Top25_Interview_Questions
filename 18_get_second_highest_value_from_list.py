## Get second highest value from list

def get_max(lst):
    lst.sort()
    return lst[-2]

print(get_max([23,54,65,98,27,45,16,83]))
