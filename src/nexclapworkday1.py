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
# 
#
#
#
print ("running s7a5")
values = []
numcount = 0
for i in range (1,6,1):
    values.append(float(input("Please give a number as a decimal.\n")))
for i in range (1,6,1):
    if values >= 90:
        numcount += 1
print(f"Your numcount is {numcount}.\n")

    
