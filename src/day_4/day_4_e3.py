# This is exercise 3, where I have to make a function called is_even(n) that returns True if the number is even, otherwise false.
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
n = int(input("please give a number.\n"))
is_even(n)
if is_even(n) == True:
    print("Your number is even.")
else:
    print("Your number is odd.")    
# This works.    
    