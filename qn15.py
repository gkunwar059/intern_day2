# 15. Write a Python program to filter a list of integers using Lambda. 

list_number=[1,2,3,4,5,6,7,8,9,10]

# num=lambda x:x%2==0 

filter_list= list(filter(lambda x:x%2==0,list_number ))
print(filter_list)