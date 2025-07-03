"""
You will be given 3 inputs 

1. starting_amount = 3000
2. yearly interest = 8 (assume it is percent -> 3000 * (8/100) )
3. number of years = 2

Your output will show Total Amount after number of years for SIMPLE INTEREST

So, first:
The yearly interest needs to be calculated,
with the code that basically says something like:
 yearly_income = "starting_amount"* yearlyinterest/100
 total_amount = numberofyears * yearlyincome + starting_amount
"""

starting_amount = 1000
yearly_interest = 10
number_of_years = 10
yearly_income = starting_amount * (yearly_interest /100)
total_amount = (number_of_years * yearly_income) + starting_amount
print(total_amount)