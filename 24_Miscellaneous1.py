"""
Python code to convert given list:[1,2,3,4,5,6,7] to output=[[1,2,3],[4,5,6],[7]]
"""


def conv_sub(lst, max_size):
    out = []
    for i in range(0, len(lst), max_size):
        out.append(lst[i:i+max_size])
    print(out)

conv_sub([1, 2, 3, 4, 5, 6, 7], 3)

