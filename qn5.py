# 5. Write a Python function to calculate the factorial of a number (a non-negative 
# integer). The function accepts the number as an argument. 

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

number=5

print(factorial(number))