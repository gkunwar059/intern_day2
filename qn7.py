# 7. Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters. 
# Sample String : 'The quick Brow Fox' 
# Expected Output : 
# No. of Upper case characters : 3 
# No. of Lower case Characters : 12 


sample_string="The quick Brown Fox"
def get_string(string):
    upper=0
    lower=0
    for item in string:
        if item.isupper():
            upper +=1
        if item.islower():
            lower +=1
    print( f"No. of Upper case characters: {upper} ")
    print(f"No. of Lower case Characters :{lower}")

get_string(sample_string)




