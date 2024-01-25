# str1 = "abmitabaa"

# first = str1[0]

# str1 = str1.replace(first,"$")


# new_str = str1.replace("$",first,1)
# print(new_str)

# str1 = "Hello"
# str2 = "rabindra"
# first1 = str1[:2]
# first2 = str2[:2]

# str1 = str1.replace(first1,first2,1)
# str2 = str2.replace(first2,first1,1)
# new_str = str1 + ' ' + str2
# print(new_str)

# 9. Write a Python program to change a given string to a new string where the first 
# and last chars have been exchanged. 

# str1 = input('Enter any string: ')

# first = str1[0]

# last = str1[-1]

# str1 = str1.replace(first,last,1)

# str1=str1[::-1]

# str1 = str1.replace(last,first,1)

# str1=str1[::-1]
# print(str1)

# 11. Write a Python program to count the occurrences of each word in a given 
# sentence. 

# string = "Hello ramesh Hello Ganesh"
# char_list = []
# dict1 = {}

# for st in range(len(string)):
#   if string[st] in char_list:
#     dict1[string[st]] = dict1[string[st]] + 1

#   else:
#     char_list.append(string[st])
#     dict1[string[st]] = 1

# print(char_list)
# print(dict1)


# 19. Write a Python program to get the smallest number from a list. 

str1 = "1 2 3 4 5 6"
numbers_list = str1.split(' ')
list1 = map(lambda x: int(x), numbers_list)
print(max(list1))

