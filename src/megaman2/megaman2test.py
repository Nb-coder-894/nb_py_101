# This the test zone for the features such as save, load, run, and to add things to the player data, along with the original battle experience.
# Now trying to test the dictionary player data add function.

# player_data = {
#     "Weapons" : ["Mega_buster"]
# }
# print("Now running player data add mode.")
# no = int(input("nonumberger1"))
# if no == 1:
#     player_data["Weapons"].append("Quick_Boomerang")
#     print(player_data["Weapons"])

# Note to future self. When calling stuff from a dictionary, always use square brackets.
# Alright, so to add stuff to the list, you have to basically append the called list (see line 9) outside of the dictionary calling. That's gud to know.
# Okay, time to go to the old document to see how things run.
# I have ported the entire code here, in order to figure out on this python document how to do the whole combat, moving, and fighting, and jumping experience. 
# Should something go wrong here, I have the entire document unchanged on megaman2.py.

# import time
# print("Now running Megaman version 1.0.0")
# time.sleep(2.3)
# print("You are Megaman. \n You were created by Dr.Light to stop the evil intentions of Dr.Wily. \n However, after you were created, Dr.Wily created 8 Robo Masters, and sent them after you. \n You must stop them, with the aid of your Mega Buster.")
# time.sleep(3.4)
# player_data = {"Health" : 100,
#                "Weapons" : ["Mega Buster"],
#                "Stages_Cleared" : [],
#                "Wily_Tower_Mode" : False,
#                "x_position" : 0,
#                "y_position" : 0,
#                "battle_mode" : False

#                }    
# print("Now entering stage select")
# time.sleep(0.001)
# while True:
#     # Note that this while true is to be used for stage select later on
#     stage_select = input("Which stage will you chose?\n Your options are Bubble Man, Metal Man, Air Man, Crash Man,\n Flash Man, Heat Man, Quick Man, and Wood Man. \n Type in the name of the Robo Master you would like to fight. \n Oh, and please note: You cannot just go and fight them. They are in 8 different areas around the world, and you must navigate their stages in order to fight them. \n ")
#     stage_select = stage_select.lower()
#     if stage_select == "flash man":
#         print("Now loading Flash Man stage...\n")
#         time.sleep(4.1)
#         print("You are now in Flash Man's stage.")
#         print("You are currently in an area with slick stones.")
#         time.sleep(2)
#         while True:
#             # Note that this while true is for the action request when not currently in a battle
#             action_request = input("What would you like to do? Jump using j? Move using m?\nEquip weapon using w? ")
#             action_request = action_request.lower()
#             if action_request == "m":
#                 while True:
#                     # Note that this while true is for the move request direction checker    
#                     move_direction = input("Okay, forward or backward?\n You can type in f for forward and b for backward.")
#                     move_direction = move_direction.lower()
#                     if move_direction == "f":
#                         player_data["x_position"] += 1
#                         print("Okay. You moved forward.")
#                         break
#                     elif move_direction == "b":
#                         print("Loading...")
#                         if player_data["x_position"] - 1 < 0:
#                             print("You cannot go back from here.")
#                         else:
#                             print("Okay. You moved backward.")
#                             player_data["x_position"] -= 1
#                     else:
#                         print("ERROR\nCOMMAND NOT UNDERSTOOD\n PLS TRY AGAIN")        
#             elif action_request == "w":
#                 print("Your available weapons are:\n" + str(player_data["Weapons"]))
#             elif action_request == "j":
#                 print("Developer's note:\n the jump function in this game will make you jump one space higher and one space forward at the same time.\n However, you won't stay in the air, so you will end up falling back to where you were. \n This is why your altitude will not change regardless of whether you jump or not.\n")
#                 print("You jumped, and were unable to stay in the air.\n Thus, you fell back down, but managed to move forward.")    
#                 player_data["x_position"] += 1
#             else:
#                 print("ERROR\n COMMAND NOT UNDERSTOOD\n PLS TRY AGAIN")
#             if player_data["x_position"] == 5:
#                 player_data["battle_mode"] == True
#             if player_data["battle_mode"] == True:
#                 print("An enemy approaches!")
#             time.sleep(3.32123123311313131321)
#             print("You are now fighting a ChuckBot.\n What will you do? Attack using w? Or try to run using r?")                    

# Houston, we have a problem.
# In this version of the code, there are no functions, meaning that every single time the player
#...types the command to move, the chuckbot attack occurs, but does not result in the battle mode activating and locking the player into the rpg mode
#...that this version was made for. Time to make a version from the original megaman2.py using functions.
import time
import random
print("Now running Megaman version 1.0.0")
time.sleep(2.3)
print("You are Megaman. \n You were created by Dr.Light to stop the evil intentions of Dr.Wily. \n However, after you were created, Dr.Wily created 8 Robo Masters, and sent them after you. \n You must stop them, with the aid of your Mega Buster.\n To stop them, you must travel to 8 diferent areas around the world,\n and you must navigate their stages in order to fight them. \n ")
time.sleep(3.4)
player_data = {"Health" : 100,
               "Weapons" : ["Mega Buster"],
               "Stages_Cleared" : [],
               "Wily_Tower_Mode" : False,
               "Battle_Mode" : False,
               "Boss_Battle_Mode" : False, 
               "Stage_Select" : True,
               "Flash_Man" : False,
               "Metal_Man" : False,
               "Heat_Man" : False,
               "Bubble_Man" : False,
               "Quick_Man" : False,
               "Crash_Man" : False,
               "Adventure_Mode" : False,
               "x_pos" : 0,
               "y_pos" : 0
               

               }

def check_stage_select(pseudo_stage_select):
    if pseudo_stage_select["Stage_Select"] == True:
        print("Now entering stage select")
        time.sleep(0.001)
        stage_select = input("Which stage will you choose?\n Your options are Bubble Man, Metal Man, Air Man, Crash Man,\n Flash Man, Heat Man, Quick Man, and Wood Man. \n Type in the name of the Robo Master you would like to fight. \n ")
        stage_select = stage_select.lower()         
        if stage_select == "flash man":
            pseudo_stage_select["Flash_Man"] = True
            pseudo_stage_select["Stage_Select"] = False
        else:
            print("COMMAND NOT UNDERSTOOD.\n PLEASE TRY AGAIN")
            stage_select = input("Which stage will you choose?\n Your options are Bubble Man, Metal Man, Air Man, Crash Man,\n Flash Man, Heat Man, Quick Man, and Wood Man. \n Type in the name of the Robo Master you would like to fight. \n ")
            stage_select = stage_select.lower()
            pass   
check_stage_select(player_data)
def check_all_levels(psuedo_level):
    if psuedo_level["Flash_Man"] == True:
        print("Now loading Flash Man Stage...\n")
        time.sleep(0.1)
        psuedo_level["Adventure_Mode"] = True
check_all_levels(player_data)        
def zone_check(psuedo_zone_checker):
    if psuedo_zone_checker["Flash_Man"] == True and psuedo_zone_checker["Adventure_Mode"] == True:
        print( "=" * 100 ,  "\nLoad Complete.\n")
        time.sleep(0.15)
        print("Now in Flash Man beginning stage.\n")
        while psuedo_zone_checker["Flash_Man"] == True:
            move_select = input("What will you do? Move using m? Jump using j? or check weapon using w?").lower()
            if move_select == "m":
                move_select_directional_pos = input("Okay, forward or backward? You can use f or b to explain that.").lower()
                if move_select_directional_pos == "f":
                    print("Okay. You choose to move forward.")
                    print(f"TESTING \n Your x_pos is {psuedo_zone_checker["x_pos"]})
                    psuedo_zone_checker["x_pos"] += 1
                if move_select_directional_pos == "b":
                    while True:
                        if psuedo_zone_checker["x_pos"] == 0:
                            print(" You can't go back from here.\n This is the starting area.")
                            
            elif move_select == "w":
                print("You have" + psuedo_zone_checker["Weapons"])
            elif move_select == "j":
                print("Okay, you choose to jump. You moved forward.")                
    else:
        print("ERROR 400")
        time.sleep(1.2)
        
        print("Now redirecting into stage select...")
        check_stage_select(player_data)    
zone_check(player_data)
def location_checker(location_checker):
    while True:
        if location_checker["x_pos"] == 5:
            location_checker["Battle_Mode"] = True
            print("!" * 100)
            print("!" * 100)
            print("!" * 100)
            print("!" * 100)
            print("An enemy approches. You are now fighting a ChuckBot.")

                               

