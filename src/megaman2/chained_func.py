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

number = int(input("Please give a number"))
def main(odd_or_even):
    if odd_or_even % 2 == 0:
        print("Start Run")
        def soemthing(arithmetic_Progression_maker_even):
            n = (100-arithmetic_Progression_maker_even) / arithmetic_Progression_maker_even + 1
            print(n)
            n = int(n)
            for i in range(1,n):
                # Note: For each of the terms, 2,4,6,8,all the way to 50.
                # The program can correctly identify the number of terms for an even sequence of numbers going from that number until 100.
                # However, it cannot make the arithmetic progression so far. 
                arithmetic_progression = [2]
                arithmetic_progression.
            print(arithmetic_progression)    
        soemthing(number)
           
"""
"""
 

if __name__ == "__main__":
    main(number)