# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7) 
# Expected Output : -336 


sample_list=[8, 2, 3, -1, 7]

def mul_num(sample_list:list):
    mul_num=1
    for number in sample_list:
        mul_num *=number
    print(mul_num)

mul_num(sample_list)