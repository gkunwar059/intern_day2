# 18. Write a Python program to check whether a given string is number or not 
# using Lambda. 

# python have inbuilt function to check the string is number or not 
# "is" - string or not 
# "0022"-string or number

# s.s.isdigit

is_number= lambda s:s.isdigit()
print(is_number('Ram'))
print(is_number('1234'))
