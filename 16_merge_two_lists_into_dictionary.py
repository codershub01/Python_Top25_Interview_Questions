## Merging out two lists into a dictionary

def merge_list(lst1, lst2):
    d = {}
    for i,j in zip(lst1, lst2):
        d[i]=j

    return d

print(
    merge_list(
        ["name", "city", "email", "designation"],
        ["Rohit", "Delhi", "rs@yopmail.com", "Sr. Software Engineer"]
    )
)
