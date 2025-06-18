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







































"""