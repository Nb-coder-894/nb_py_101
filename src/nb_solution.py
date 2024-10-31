""""
write your thought process here
# Think:
"""# Think:
## You are given a list as [1,2,3,4,5,6,7]
## Write python code to output numbers from this list if they are odd
## output should print those numbers
## pseudocode is enuf

input = [1, 2, 3, 4, 5, 6, 7]

# what is a list in python ? google/cgpt
# How to iterate over a list
# 

# So, if you can print using a for loop, then make 

# Start reading the loop

# With the loop variable, modulus it by 2, if the moldulo is equal to 1, then print the number, else bypass.
for i in input:
    modulo_val = i % 2
    if modulo_val == 1:
        print (i)  
    else:
        continue     