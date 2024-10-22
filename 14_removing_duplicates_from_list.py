## Removing all duplicated values from a list


def removing_duplicates(lst):
    lst_= []
    for i in lst:
        if i not in lst_:
            lst_.append(i)
    lst = lst_
    del lst_
    return lst

print(removing_duplicates([11,22,34,2,5,71,11,53,22,2]))