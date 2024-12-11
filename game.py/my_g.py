#Class notes for 12-3-24
import random
import time
# choose a number 1-10 and save it as variable
# print the game name
# ask user for number
# if number is correct, say correct and end
# if the number incorrect, give more try. If 5 tryies done then say lose. 
answer_s = random.randint(1,10)
print ("Guessing game.")
time.sleep(1)
tries = 5
while tries > 0:
    print("What is the number?")
    time.sleep(15)
if input == answer_s:
    print("correct. You win!! Congratulations!")
elif input != answer_s:
    print("Incorrect")    
if tries == 0:
    print("end")        













#MYWORK