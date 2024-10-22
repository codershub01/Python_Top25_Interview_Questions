## Count no. of white-spaces available in a string


def count_wspaces(string):
    cnt = 0
    for i in string:
        if i == " ":
            cnt += 1

    print(f"No. of white spaces in given string :: {string} are {cnt}")

count_wspaces("hey! welcome to the world of codes  ")