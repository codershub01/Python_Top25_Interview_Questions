## Reverse a given number

def reverse_int(num):
    print("Given Num :", num)
    rev_int = 0
    while num!=0:
        rem = num % 10
        rev_int = rev_int*10 + rem
        num //=10

    print("Reversed Num :", rev_int)

reverse_int(4356)