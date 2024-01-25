# 1. Write a Python function to find the Max of three numbers. 



def find_max(a,b,c):
  max_number = max(a,b,c)
  print(max_number)



# 2. Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7) 
# Expected Output : 20 


def sum_list(list1):
  sum_lst = sum(list1)
  print(sum_lst)

sum_list([1,4,5,5])


    
# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7) 
# Expected Output : -336 


from functools import reduce

list1 = [1,4,5,-5]
result = reduce(lambda x,y: x*y, list1)
print(result)


    
# 4. Write a Python program to reverse a string. 
# Sample String : "1234abcd" 
# Expected Output : "dcba4321" 


def reverse_string(str1):
  str1 = str1[::-1]
  print(str1)
reverse_string('a,23,3')


    
# 5. Write a Python function to calculate the factorial of a number (a non-negative 
# integer). The function accepts the number as an argument. 


def fact(n):
  if n == 1:
    return 1
  else:
    return n*fact(n-1)

print(fact(4))





# 6. Write a Python function to check whether a number is in a given range. 


def is_in_range(num, range_value):
  return num in range(range_value)

print(is_in_range(5,100))



# 7. Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters. 
# Sample String : 'The quick Brow Fox' 
# Expected Output : 
# No. of Upper case characters : 3 
# No. of Lower case Characters : 12 


a='stRiNgS HahA'
upperCount = 0
lowerCount = 0
otherCharacters = 0

def count_upper_lower(a):
  for i in range(len(a)):
    if ord(a[i])>=65 and ord(a[i])<=90:
      global upperCount
      upperCount += 1
    elif ord(a[i])>=97 and ord(a[i])<=122:
      global lowerCount
      lowerCount += 1
    else:
      global otherCharacters
      otherCharacters += 1

  print('Upper count ',upperCount)
  print('Lower count ',lowerCount)
  print('Lower count ',otherCharacters)

count_upper_lower(a)


    
# 8. Write a Python function that takes a list and returns a new list with unique 
# elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5] 
# Unique List : [1, 2, 3, 4, 5] 



def unique_list(lst):
  return list(set(lst))

print(unique_list([1,2,3,4,1,2,3,4,22,2,2,3,4,5,]))



    
# 9. Write a Python function that takes a number as a parameter and check the 
# number is prime or not. 
# Note : A prime number (or a prime) is a natural number greater than 1 and that 
# has no positive divisors other than 1 and itself. 


count = 0

def isPrime(num):
  for i in range(1,num+1):
    if num%i == 0:
      global count
      count = count + 1
  
  if count > 2:
    print('It is not a prime number')
  else:
    print('It is a prime number')

input1 = int(input('Enter any number other than 0 and 1: '))
isPrime(input1)



# 10. Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Result : [2, 4, 6, 8] 


num_list = [1,2,3,4,6,7,3,3,5,7,4,3,4,4,5,5]

even_list = filter(lambda x: x%2 == 0, num_list)
print(list(even_list))



    
# 11. Write a Python program to create a lambda function that adds 15 to a given 
# number passed in as an argument, also create a lambda function that multiplies 
# argument x with argument y and print the result. 



add_result = lambda x: x+15

mul_result = lambda x,y: x*y

print(add_result(2))
print(mul_result(2,4))



# 12. Write a Python program to create a function that takes one argument, and 
# that argument will be multiplied with an unknown given number. 



mul_result = lambda x: x*10
print(mul_result(2))



# 13. Write a Python program to sort a list of tuples using Lambda. 


list1 = [(1,2), (2,1), (3,4), (4,3), (2,2), (1,99), (77,33), (5,9), (9,29), (4,1), (7,2)]

list1 = sorted(list1, key = lambda x: x[0])
print(list1)



# 14. Write a Python program to sort a list of dictionaries using Lambda. 



list_to_be_sorted = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 
print(newlist)




# 15. Write a Python program to filter a list of integers using Lambda. 



list1 = [1,2,3,4,2,32,3]

filter_list = filter(lambda x: x%2 == 0, list1)

print(list(filter_list))



# 16. Write a Python program to square and cube every number in a given list of 
# integers using Lambda. 


list1 = [1,2,3,4,5]

square_num = map(lambda x:x*x, list1)
cube_num = map(lambda x:x*x*x, list1)

print(list(square_num))
print(list(cube_num))



# 17. Write a Python program to find if a given string starts with a given character 
# using Lambda. 


input1 = input('Enter any string: ')
input2 = input('Enter any character: ')

check = lambda x,y: x[0] == y
if check(input1, input2):
  print(f'Yes, the string starts with "{input2}"')
else:
  print(f'No, the string does not start with "{input2}"')



# 18. Write a Python program to check whether a given string is number or not 
# using Lambda. 


import re

input1 = input('Enter any string: ')
regex = '[+-]?\d+\.?\d*'

isNumber = lambda input1: re.search(regex, input1)

if isNumber(input1):
  print(f'Yes the string is a number')
else:
  print('No the string is not a number')




# 19. Write a Python program to create Fibonacci series upto n using Lambda. 


from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

n = int(input('Enter any number: '))
print(fib_series(n))



# 20. Write a Python program to find intersection of two given arrays using 
# Lambda. 


array1 = [1,2,3,4,3,5,3,3,3]
array2 = [2,4,5,7,8,9,4,3,2,3,4,5,5]

result = list(filter(lambda x: x in array1, array2)) 

intersection_array = list(set(result))
print(intersection_array)