"""
# Understanding continue and pass 

 - What `continue` statement does in a for loop
 - What `pass` statement does in a for loop

## Problem

Input is a list `[ 1, 2, 3, 4, 5, 6, 7, 8 ]`
Write a code that will multiply 10 with odd numbers
Expected output 10, 30, 50, 70  and also print original number +1
Wrte another code that will get out of for loop if any even number greater than 4 is encountered
"""

list_variable = [1, 2, 3, 4, 5, 6, 7, 8]

for i in list_variable:
    if i % 2 == 1:
        print(i * 10)
    else :
        pass
    print(f"original number is ->> {i} and + 1 is  ---> {i+1}")