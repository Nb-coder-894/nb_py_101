import random
import time
print("Would you like hard or easy?")
if input == "hard":
    answer_s = random.randint(1,10)
# Choose a number 1-10 and save it as a variable
elif input == "easy":

    answer_s = random.randint(1, 10)

# Print the game name
print("Guessing game.")
time.sleep(1)

# Initialize number of tries
tries = 5

while tries > 0:
    print(f"You have {tries} tries left.")
    # Ask the user for a guess
    guess = int(input("What is the number? "))  # Convert input to an integer
    
    # Check if the guess is correct
    if guess == answer_s:
        print("Correct! You win!! Congratulations!")
        break
    else:
        print("Incorrect.")
    
    # Decrease the number of tries after an incorrect guess
    tries -= 1

# If the loop finishes without a correct guess
if tries == 0:
    print("Game over. You lost. The correct number was", answer_s)
    
