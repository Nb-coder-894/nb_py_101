# This is exercise 2 for the 2nd print edition of day 5, where I have to make...
# A math wizard power using the quadratic equation ax^2+b+c = 0.
num1 = int(input("Please give num1\n"))
num2 = int(input("Please give num2\n"))
def make_quad(num1, num2):
    a = num1 + num2
    b = num1 * num2
    if a < 0 and b < 0:
        print(f"x^2 {a}x {b}")
    elif a < 0:
        print(f"x^2 {a}x +{b}")
    elif b < 0:
        print(f"x^2 + {a}x {b}")
    else:            
        print(f"x^2 + {a}x + {b}")
make_quad(num1, num2)
# After multiple attempts, I managed to make this work.
# I also learned how to call local variables using the curly brackets.
# Job done. -Nb    