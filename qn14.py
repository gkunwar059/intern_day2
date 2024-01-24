# 14. Write a Python program to sort a list of dictionaries using Lambda. 


dicto_1={1:3,4:5,9:2,2:9}

# concept for the sorted the dictonaries using the lambda function
sorted_dict= sorted(dicto_1.items(),key= lambda x:x[0])
print(dict(sorted_dict))