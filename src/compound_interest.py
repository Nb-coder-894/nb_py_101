initial_amt = 1000
interest_rate = 10
number_of_years = 3


for i in range(number_of_years): 
    compound_variable = initial_amt * (interest_rate/100)
    initial_amt += compound_variable
print(initial_amt)    



