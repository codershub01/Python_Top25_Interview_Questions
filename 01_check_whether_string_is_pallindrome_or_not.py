def check_pallindrome(strng):
    if strng.lower() == strng[::-1].lower():
        print("The given string is Pallindrome")
    else:
        print("The given string is not Pallindrome")

check_pallindrome("radar")
# check_pallindrome("check")

