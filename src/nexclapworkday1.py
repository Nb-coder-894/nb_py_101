# """
# Nexclap set 7 activity 1.
# for loop from 30 to 300 printing every other number
# for i in range (30,300,2):
#     print(i)
# Set 7 act.2:
# for loop from 500 to 30, printing every other number
# for i in range (500,30,-2):
#     print(i)
# Set 7 act 3:
# for loop from 1,000 to 1 printing every 3rd number.
# for i in range (1000,1,-3):
#     print(i)
# Set 7 act 4:
# for loop from 1 to 15 printing only multiples of 3
# for i in range(1,15):
#     if i%3 == 0:
#         print(i)
# # """
# Set 7 act 5:
# make user input 5 decimal values. Put this in a list called values. Loop through the list and put how many of the numbers are between 10 and 100/
# print ("running s7a5")
# values = []
# numcount = 0
# for i in range (1,6,1):
#     values.append(float(input("Please give a number as a decimal.\n")))
# for i in range (0 ,len(values),1):
#     if values[i] >= 90 and values[i] <= 110:
#         numcount += 1
# print(f"Your numcount is {numcount}.\n")
# Notes about this:
# the reason that there is a values[i] thing there is because it has to loop through the list, and len(values) because that is the length of the list values, so that the for loop is as efficient as possible.
# Set 7 act 6
#Ask the user to input 5 decimal values. Add them to a list called vals. print the total sum of all of the elements in the list.
# print("Now running s7a6")
# vals = []
# for i in range (0,5,1):
#     vals.append(float(input("Please give a decimal.\n")))
#     summation = vals[i]+vals[i]+vals[i]+vals[i]+vals[i]
# print(summation)    
#Set 7 act 7
# samething as last time, but now multiply all of the terms.
# vals = []
# for i in range (0,5,1):
#     vals.append(float(input("Please give a decimal.\n")))
#     product = vals[i]*vals[i]*vals[i]*vals[i]*vals[i]
# print(product)
#Set 7 act 8
# Now, ask for 5 decimal values. Add them to a list called vals. If one of the numbers in the list is 10 AND the numbers in the list sum to 10, print that "10 is present in this list". Otherwise, print "10 is not present in this list."
# print("Now running s7a8")
# vals = []
# for i in range (0,5,1):
#     vals.append(float(input("Please give a decimal.\n")))

# isTen = False

# for x in range(0, len(vals), 1):
#      if vals[x] == 10:
#         isTen = True
# if isTen and sum(vals) == 10:
#      print("10 is present in this sequence.")
# else:
#     print("10 is not present in this sequence.")          
#Set 7 act 9
#samething as last time, only that there is an "or" statement instead of an "and statement".
# print("Now running s7a9")
# vals = []
# for i in range (0,5,1):
#     vals.append(float(input("Please give a decimal.\n")))
# hasTen = False
# for z in range (0, len(vals),1):
#     if vals[z] == 10:
#         hasTen = True
# if hasTen or sum(vals) == 10:
#     print("10 is present in this sequence.")
# else:
#     print("10 is not present in this sequence.")
# Set 7 act 10
# ask for 5 decimals. If the first and last terms of the decimal inputs are equal to each other, then print that the first and last terms are equal. Otherwise, print that they are not equal.
# print("Now running s7a10")
# vals = []
# for i in range (0,5,1):
#     vals.append(float(input("Please give a decimal.\n")))
# if vals[0] == vals[4]:
#     print("The first and last terms are equal to each other.")
# else:
#     print("The first and last terms are not equal to each other.")  
# Set 7 act 11
# Get 5 decimals, add them to a list called values, then check if they are within 10 of 100 OR 200. Pretty simple compared to the past few activities.
# print("Now running s7a11")
# values = []
# correct = 0
# for i in range (0,5,1):
#     values.append(float(input("Please give a decimal. \n")))
# for i in range (0, len(values),1):
#     if values[i] <= 110 and values[i] >= 90:
#         correct += 1
#     elif values[i] <= 210 and values[i] >= 190:
#         correct += 1
# print(f"You have {correct} correct numbers.")  
# Set 7 act 12
# Get 5 decimal values, add them to a list called "values". However, add all of the terms into a list called "reversed", which has all of the same values but reversed.
# print("Now running s7a12")
# values = []
# for i in range (0,5,1):
#     values.append(float(input("Please give a decimal.\n")))
# reversed = values[::-1]
# print(reversed)
#set 7 act 13
#Sum up all 5 decimals, then check if the sum is less than or greater than 50, and print that.
print("Now running s7a13")
values = []
for i in range (0,5,1):
    values.append(float(input("Please give a decimal.\n")))
if values[i].sum() >= 50:
    print ("The sum of the decimals is greater than 50.")
elif values[i].sum() <= 50:
    print("The sum of the decimals is less than 50.")
else:
    print("Yeah... it's probably equal to 50.")        


           
 

