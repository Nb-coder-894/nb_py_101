# import random
# import time
# print("Now running the superspecial productivity module v.1.0.0.0...\n")
# outdoor_time_y = random.randint(1,60)
# Total_outdoor_time = outdoor_time_y + 60
# print(f"Your total outdoor time for the day is:{Total_outdoor_time}")

# This would have been useful, only it doesn't really help that much.
# It would have been more useful if it put it into hours and minutes
# Let's try something else
import random
import time
print("Now running the superspecial producivity module v.1.0.0.1\n")
time.sleep(2)
while True:
    productivity_choice = input("What do you intend to use? \n \n \n You may: \n \n \n \n \n use the outdoor activity module to \n calculate the outdoor duration by typing in either outside or o in the bar: \n\n\n\n\n\n\n or you may calculate your set indoor duration by typing in (i) (just the letter pls) in the bar. ")
    productivity_choice == productivity_choice.lower()
    if productivity_choice == "o" or productivity_choice == "outside":
        print("Very well.")
        time.sleep(2)
        outdoor_constraint_1 = int(input("How long will the definite time of outdoor last, \n before the random additon? \n"))
        outdoor_randtime = random.randint(1,45)
        total_outdoor = outdoor_constraint_1 + outdoor_randtime 
        formal_total_outdoor_hr = total_outdoor // 60 
        formal_total_outdoor_min = total_outdoor % 60
        print(f"Your converted time has been calculated as {formal_total_outdoor_hr}hrs and \
    {formal_total_outdoor_min}mins. \n It's also {total_outdoor} mins.")
        continue_request = input("Would you like to use it again? (y/n) \n")
        continue_request = continue_request.lower()
        if continue_request == "y":
            time.sleep(2)
            continue
        else:
            break
    elif productivity_choice == "i":
        print("Very well.")
        indoor_preset_time = input("What will be the indoor preset time? pls put in mins")
        indoor_preset_mins = indoor_preset_time % 60
        indoor_preset_hrs = indoor_preset_time // 60

    else:
        print("I'm sorry. Your command is not understood, please try again?\n")
        time.sleep(1)
        continue
         
