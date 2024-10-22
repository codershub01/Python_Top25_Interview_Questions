## Count no. of special characters in a string

def count_schars(string):
    cnt = 0
    for i in string:
        if i  in '~!@#$%^&*()_+-={}|[]\:;<>?,./':
            cnt+=1
    print(f"No. of special characters in given string :: {string} are {cnt}")

count_schars("Rsharma@%$#@!^")