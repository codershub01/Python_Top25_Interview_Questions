## Merging two lists

def merge_list(lst1, lst2):
    return lst1 + lst2


    """
        ## Alternative
        lst1.extend(lst2)
        return lst1    
    """

print(merge_list([12,54,62,43],[23,87,47,31]))