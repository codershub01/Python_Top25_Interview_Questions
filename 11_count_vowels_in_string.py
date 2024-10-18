## Count no. of vowels present in a string.

def count_vowels(str1):
    cnt = 0
    for i in str1:
        if i in list('aeiou'):
            cnt += 1
    print(f"No. of vowels in a given string -> {str1} is {cnt}")

count_vowels("Rohit")

