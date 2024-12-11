import random
import time

answer_s = random.randint(1,10)
print("Guessing game.")
time.sleep(1)
tries = 5
while tries > 0:
    print(f"You have {tries} left")
the_guess = int(input("What is the number?"))
if the_guess == answer_s:
    print("correct")


if tries == 0:
    print("fail")
    