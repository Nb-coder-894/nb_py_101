"""
Learning about substrings and Taking characters from a string.

substrings are parts of a string that can be assigned to a variable.

For example:

word = "abcdefgh"

x = word[0:3]

print(x)

# This will create an output of "abc"

y = word[0]

# This will create an output of "a".

#2: How to choose random items from a list. 
#To choose random items from a list, first import randint.

from random import randint

items = ["apple", "banana", "orange"]

randomVal = randint (0,2)

x = items[randomVal]

print(x)

#This will create a random series of "apple", "banana", etc.

#3: Choosing random characters from a string.

#This is pretty similar to the last thing, but with a single string. I would think that this would combine the effects of substrings and randint.

from random import randint

word = "Three"

randomVal = randint(0,2)

x= word[randomVal]

print(x)

#This will result in the code giving a sandom letter, based on the randfint function.

#4: Adding a character to an existing string.
# This wil prbably use slicing to add letters to a string.

x = "dinosaur"

x = x + "s"

print(x)

#Output: dinosaurs

y = "h"

for x in range(0,10,1):
    y = y + "h"
print(y)
#Output: hhhhhhhhhhhhhhhh 

#Set 1 Exercise:
# Converting DNA to RNA to Amino Acid conversion
#Requirements:
# Ask the user to input the length of a DNA sequence.
# THe possible characters for the DNA seqence are ATCG.
# Make sure it is random THough.
# So, it has to be a random seqence of those four letters for the given length from the user.
#Optional: using RNA, convert into amino acids.
#Notes: A in Dna becomes U in Rna
# T in DNA becomes A in RNA
C in DNA becomes G n RNA
G in DNA becomes C in RNA

So, I'll make a list and use splicing to make it.
from random import randint
Dna_Length = int(input("Please give the number of DNA sequence. \n"))
DNA = "ATCG"
for i in range (0,Dna_Length):
    x = randint(0,3)
    Randomval = DNA[x]
    if Randomval == "T":
        RNAval = "A"
    elif Randomval == "C":
        RNAval = "G"
    elif Randomval == "G":
        RNAval = "C"
    else:
        RNAval = "U"
    print("Your RNA value is:\n")
    print(RNAval) 
# Finding average value of a list:
# To find the average (arithmetic mean) of a list, do the following code:
numbers = [1,2,3,4]
x = sum(numbers)

#Finding the length of a list using the len function

y = len(numbers)

#result

print(x/y)

# This concludes how to find the average of a list.

# How to print all of the numbers divisible by 4 between 1-100.
# You would use the modulus operator in order to find this, as shown:

#Firstly, remember that is I do 10 % 2, the answer is 0 (not 5), because 10 is divisible by 2 evenly and thus has no remainder. As this is a recap from what I already know, I will not mention more about it.
#Here's the code to do that:

#Use a for loop and modulus

for i in range (1,101,1):
    if x % 4 == 0:
        print(x)

# Pretty simple code.
# Next task: Set 2 exercises:
# s2a1: create a for loop from 1 to 1,000, printing every 3rd number.
print("Now running s2a1")
for i in range (3,1000,3):
    print(i)
s2a2
create a for loop from 30 to 350 printing every even number.
print("Now running s2a2")
for i in range (28,352,2):
    print(i)
s2a3
create a for loop from 200 to -200 printing multiples of 3.
print("Now running s2a3")
for i in range (-200,200):
    if i % 3 == 0:
        print(i)
s2a4
#create a for loop from 1 to 1,000, printing only the multiples of 7.  
print("Now running s2a4")
for i in range (1,1000):
    if i % 7 == 0:
        print(i)
s2a5
#create a program that will ask your score out of 120 and then give you your percentage based on how well you did.
#Here is the gradation scale: 
A is the 90% or above.
B is 80% to 89.9%.
C is 70% to 79.99%
F is below 70%
print("Now running s2a5")
import time
while True:
    score = float(input("Out of 120, how much did you get? \nIf you got 'x' out of 120 then put that x value, such as 12 or 120.\n If you recieved a decimal score, such as 99.5 out of 120, this code will still take it. \n "))
    score = (score/120)*100

    if score >= 90:
        print(f"Congrats! You got an A, which is the highest score that you could get. \n No improvement necessary!\n Your percentage was {score}%.")
    elif score >= 80 and score <= 89.9:
        dif = 90 - score
        dif  = (dif * 120)/100
        print(f"You got a B. \n To get the next highest score, you would need {dif} more percent. \n Your percentage was {score}%.")
    elif score>=70 and score <= 79.99:
        dif = 80 - score
        dif = (dif*120)/100
        print(f"You got a C.\n To get the next highest score, you would need {dif} more points. \n Your percentage was {score}%.")
    else:
        dif = 70 - score
        dif = (dif*120)/100
        print(f"You got an F. \n You have failed. \n To get the next highest score, which is a C, you would need {dif} more points.\n Your percentage was {score}%.")
    time.sleep(1)
    end_request = input("Would you like to leave the experience? type in y or n.")
    end_request = end_request.lower()
    if end_request == "y":
        break
s2a6
Ask the user to input their favorite basketball team.
Print out whether it is in the Eastern or Western Conference.
You can use the sample lists below that have all of the team names already:
Warriors- Western
Lakers - Western
Celtics - Eastern
Cavaliers - Eastern
eastern = ["Hawks", "Celtics", "Hornets", "Bulls", "Cavaliers", "Pistons", "Pacers", "Heat", "Bucks", "Nets", "Knicks", "Magic", "76ers", "Raptors", "Wizards"]
western = ["Mavericks", "Nuggets", "Warriors", "Rockets", "Clippers", "Lakers", "Grizzlies", "Timberwolves", "Pelicans", "Thunder","Suns", "Trail Blazers", "Kings", "Spurs", "Jazz"]
print("Now running s2a6")
western = ["Mavericks", "Nuggets", "Warriors", "Rockets", "Clippers", "Lakers", "Grizzlies", "Timberwolves", "Pelicans", "Thunder","Suns", "Trail Blazers", "Kings", "Spurs", "Jazz"]
eastern = ["Hawks", "Celtics", "Hornets", "Bulls", "Cavaliers", "Pistons", "Pacers", "Heat", "Bucks", "Nets", "Knicks", "Magic", "76ers", "Raptors", "Wizards"]
team = input("Input ur team name \n")
if team == western:
    print(f"Your team is in the western conference.")
else:
    print(f"Your team is in the eastern conference.")   
s2a7
Create a program which asks the user for 3 numbers
representing the year, month and day e.g 1982 10 08 and then outputs in the form 8th
October 1982.
print("Now running s2a7")
year = int(input("Enter the year.\n"))
Months = ["January", "February", "March"," April", "May", "June", "July", "August", "September", "October", "November", "December"]

month = int(input("Enter the month.\n")) 
month = Months[month-1]
day = int(input("Enter the day.\n"))
print(f"{day} {month} {year}")
s2a8
Create a program that loops through the list and prints out all of the items greater than 25.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i > 25:
        print(i)  
Note:
The people revoked my access to this document.
However, because I managed to copy and paste the entire document into google drive, I still have a copy of the origin nexclap document, for each page.
Sadly, some of the tasks are no longer there (such as s2a9 and s2a8) because of some kind of copy and paste error.
On the whole, however, I still have access to the concepts that they were going to teach, even though their method of teaching was to just
Write down the code and let you play Minecraft for the entirety of the class.
-N1RV@n
Dictionaries
How to make dictionaries.
These are some dictionaries with preexisiting values:
data =  {"fruit": "orange", "vegetable" : "carrot", "beverage" : "apple juice"}
data["clothes"] = "shirt"
print(data)
The output to this data is that the entire dictionary, along with the clothes : shirt.

How to iterate through a dictionary and generate key-value pairs:
This is an easy way to iterate through a dictionary and get the key value pairs.
I would say that dictionaries can be very useful in things such as the megaman2 rpg edition game because a key, such as an ingame password, will only result in a set game result, because a key cannot have more than one value directly. Putting a list as the value is allowed though.
Interestingly, a value can be put to more than one key, which would mean that the game password or weapons equipment series would not be affected by which stage you select.
When coding a word game that only uses words and letters and inputs to run, the x_postition and y_position are merely variables, but perhaps dicitonaries can be used to determine multiple things, such as the location and weaknesses of enemies, along with the location of powerups.
Anyway, to iterate through a dictionary and generate key-value pairs, follow this code:

data =  {"fruit": "orange", "vegetable" : "carrot", "beverage" : "apple juice"}
for i in data:
   print("The key is" + str(i))
#This renders the dict key into string form, similar to the int function.
print("The value is" +  str(data[i]))
The reason that value thingy works is because first of all, data[i] represents the value of the data for the iteration, and str just converts it back into a string, as it is currently in a dicitonary format. 
to prove this, I will print out the string form of the data for a set key.
data =  {"fruit": "orange", "vegetable" : "carrot", "beverage" : "apple juice"}
print(data["fruit"])
the result is orange.
This proves that not only can dictionaries be easily used as a password and inventory, they are literally like keys that unlock "doors" with their RESPECTIVE values hidden behing them.
Many of the different and same "values" can be behind the same "door", and thus be opened by the same "key", but the values are all in the same chest, which requires that one key.
This is a good metaphor on the usage of the dictionary.
s3a1
Create two lists like the ones below.
Create a loop that iterates through the lists and adds the data to a dictionary such that the output looks like :
words = ['First', 'Second', 'Third']
numbers = [1, 2, 3]

final dictionary output - { 'First':1, 'Second':2, 'Third':3 }

"""



