## Removing all duplicates from a string

def remove_duplicates(str1):

    str2 = ''
    for i in str1:
        if i in str2:
            pass
        else:
            str2 = str2 + i

    print(f"Given String : {str1}")
    print(f"After removing duplicates : {str2}")

remove_duplicates("aaabbbbcccdddeeessrr")