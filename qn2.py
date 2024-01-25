# 2. Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7) 
# Expected Output : 20 


# list_sample=[8, 2, 3, 0, 7]
# def sum_func(list_sample):
#     sum_num=0

#     for i in list_sample:
#         sum_num +=i
#         # print(sum)  
        
#     print(sum_num)

    
# sum_func(list_sample)

# list1=[2,4,5,6,7,8,9,10]
def sum_func(list1):
    sum_list=sum(list1)
    print(sum_list)

print(sum_func([2,4,5,6,7,8,9,10]))  

