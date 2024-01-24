# 8. Write a Python function that takes a list and returns a new list with unique 
# elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5] 
# Unique List : [1, 2, 3, 4, 5] 


def unique_function(sample_list):
    new_list=[]

    for item in sample_list:
        # creating new list here
        if item not in new_list:
            new_list.append(item)
    
    return (new_list)

sample_list=[1,2,3,3,3,3,4,5] 
print(unique_function(sample_list))