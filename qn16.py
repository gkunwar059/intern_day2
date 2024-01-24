
# 16. Write a Python program to square and cube every number in a given list of 
# integers using Lambda. 


list_number=[1,2,3,4,5,6,7,8,9,10]
# for square the number of list
new_square_list=list(map(lambda x:x**2,list_number))
print(new_square_list)

new_cube_list=list(map(lambda x:x**3,list_number))
print(new_cube_list)


