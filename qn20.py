
# 20. Write a Python program to find intersection of two given arrays using 
# Lambda. 


x=[1,2,3,4,5,6]
x=set(x)
y=[3,4,5,6,7,8]
y=set(y)
# z=x.intersection(y)
# print(z)

z=lambda x,y:x.intersection(y)
print(z(x,y))