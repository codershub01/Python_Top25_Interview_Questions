
## Method 1
def reverse_str(str1):
   print(str1[::-1])

reverse_str("Coder")

## Method 2=
def reverse_str(str1):
    str_ = list(str1)
    str_ = reversed(str_)
    str_ = ''.join(str_)
    print(str_)

reverse_str("Coder")