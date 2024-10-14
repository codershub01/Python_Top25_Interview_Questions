def check_anagrams(str1, str2):
    if sorted(list(str1.lower())) == sorted(list(str2.lower())):
        print("Given strings are anagrams")
    else:
        print("Given strings are not anagrams")

check_anagrams("Hasan", "shaan")

