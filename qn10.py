# 10. Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Result : [2, 4, 6, 8] 


list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# list comprehension 
new_list=[x for x in list if x%2==0]
print(new_list)