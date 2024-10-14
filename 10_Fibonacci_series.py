## Fibonacci Series

def fibo_series(num):
    n1, n2 = 0,1
    next_num = n2
    count = 1

    while count <= num:
        print(next_num, end=" ")
        count += 1
        n1, n2 = n2, next_num
        next_num = n1 + n2
    print()

fibo_series(10)
