# 19. Write a Python program to create Fibonacci series upto n using Lambda. 


from functools import reduce


# important logic here
fib_series=lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]], range(n-2),[0,1])
#last two  element in x and add it x((x+(x[-1]+x[-2]))

print(fib_series(6))
