# 6. Write a Python function to check whether a number is in a given range. 

def check_num(n):
    lower_range=1
    higer_range=10
    if n>=lower_range and n<=higer_range:
        print("Ture ! number is in the given range")
    else:
        print("False ! number is not in the given range")

num=15

check_num(num)

