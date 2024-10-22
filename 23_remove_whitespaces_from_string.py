## Removing white-spaces available in a string


def remove_wspaces(string):
    # cnt = 0
    # for i in string:
    #     if i == " ":
    #         cnt += 1
    print(f"Given string with white-spaces ::\n    {string}\n")
    string = string.split(' ')
    string = ''.join(string)

    print(f"String after removing white-spaces ::\n    {string}\n")

remove_wspaces("hey! welcome to the world of codes  ")