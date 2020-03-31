# range(stop) takes one argument.
# range(start, stop) takes two arguments.
# range(start, stop, step) takes three arguments.

# printing a number 
for i in range(10): 
    print(i, end =" ") 
  
# using range
l = [10, 20, 30, 40] 
for i in range(len(l)): 
    print(l[i]) 

# using enumerate
for i in enumerate(l): 
    print(i[1]) 

# using range to print number 
# divisible by 5 
for  i in range(0, 50, 5): 
     print(i, end = " ") 

# incremented by 2 
for i in range(2, 25, 2): 
    print(i, end =" ") 
print() 

# incremented by -2 
for i in range(25, 2, -2): 
    print(i, end =" ") 
print() 