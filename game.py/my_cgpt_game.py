import random
import time

answer_s = random.randint(1,100)
print("Guessing game.")
time.sleep(1)
tries = 5
print(f"You have {tries} left")
the_guess = int(input("What is the number?"))
if the_guess == answer_s:
    print("correct")


if the_guess != answer_s:
    print(f"fail, you have")
    