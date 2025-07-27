"""
task:
ask for a number
if number is even
    -> it will print "start run"
    -> it will call another function that will print from that number to 100 in an arithmetic progression with cd = the same number
    -> then it will print summing 
    --> it will call another function to do the sum

if number is odd
    -> it will print "oddball out"
    -> it will do a Negative arithmetic progression starting from 100 till the number is reached
    -> it will call another function( same one as in above) to sum


"""

# Sn = ({A}n/2)*(2(a1)+(n-1)a1) ==> Summation formula
# ==> n/2 * 2a1 + A1n-a1
# ==> n/2 * a1 + a1*n (Because in this case, a1 == d.)
# An = a1 + (n-1)d ==> Formula to find the nth, or last term
# ==> (When d == a1) An = a1 + a1*n - a1
# ==> Strangely, this would mean that...

# ==> An = a1+a1*n ==> Improved Formula to Find the nth/ last term
# Now, let us say that we knew that the formula for an even number will end at 100. 
# This would mean that in order to find the summation of the terms, I would first need to find the last term, and then put it into this formula:

# n = (l-a)/a1 + 1 ==> To find the number of terms in the series. Let us first try and find that--Wait...
# That formula was already in the code.

number = int(input("Please give a number. \n"))
def main(odd_or_even):
    if odd_or_even % 2 == 0:
        print("Start Run")
        def soemthing(arithmetic_Progression_maker_even):
            no_of_terms = (100-arithmetic_Progression_maker_even) // arithmetic_Progression_maker_even + 1
            print(f"Since the first term is even, the number of terms is...\n {no_of_terms}")
            summation = no_of_terms/2 * ((arithmetic_Progression_maker_even) + arithmetic_Progression_maker_even * no_of_terms)
            summation_str = str(summation)
            print(f"Your sum is...\n {summation_str}")
        soemthing(number)      
           
"""
"""
 

if __name__ == "__main__":
    main(number)