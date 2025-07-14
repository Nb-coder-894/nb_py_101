import time
<<<<<<< HEAD:src/megaman2.py
print("Now running Megaman2 RPG edition\n Version 1.0.0")
time.sleep(1)
print("You are megaman.\n You were created to stop the evil forces of Dr.Wily.\n However, after you were created, Dr.Wily created 8 Robo Masters to stop you. \n You must defeat the evil Dr.Wily and stop all 8 of his robots from wreaking havoc \n upon the world...")
player_data = {
    "health" : 100,
    "weapons" : ["Mega Buster"],
    "stage_selected" : None,
    "Wily_Tower_Mode" : False
}
time.sleep(1)
print("Now entering stage select.\n")
player_data("stage_selected") == str(input("Which Robo Master will you defeat? \n Air Man, Crash Man, Bubble Man, Metal Man, \n Quick Man, Wood Man, Heat Man, or Flash Man? \n Oh, and please note:\n You cannot just instantly go and fight each Robo Master. \n They are in different parts of the world, and are in different areas.\n You must traverse each Robo Masters's respective domain...\n and fight your way to the boss, and then defeat the boss.\n Each boss has a secret weakness to a certain ability, but you don't know what those weaknesses are.\n Also, some of the minions of those Robo Masters also have weakness to certain abilities...\n but you don't know them (yet!)\n\n Anyway, which stage do you choose? "))
player_data("stage_selected") == player_data("stage_selected").lower()
if player_data("stage_selected") == "Flash Man":
    print("Now loading Flash Man stage...\n Get your weapons ready")
    print(player_data)

   
=======
print("Now running Megaman version 1.0.0")
time.sleep(2.3)
print("You are Megaman. \n You were created by Dr.Light to stop the evil intentions of Dr.Wily. \n However, after you were created, Dr.Wily created 8 Robo Masters, and sent them after you. \n You must stop them, with the aid of your Mega Buster.")
time.sleep(3.4)
player_data = {"Health" : 100,
               "Weapons" : ["Mega Buster"],
               "Stages_Cleared" : [],
               "Wily_Tower_Mode" : False,
               "Normal_Mode" : None,
               "Hard_Mode" : None,
               "Impossible_Mode" : None                           
               }
weapon_inventory = player_data["Weapons"]    
print("Now entering stage select")
time.sleep(0.001)
stage_select = input("Which stage will you chose?\n Your options are Bubble Man, Metal Man, Air Man, Crash Man,\n Flash Man, Heat Man, Quick Man, and Wood Man. \n Type in the name of the Robo Master you would like to fight. \n Oh, and please note: You cannot just go and fight them. They are in 8 different areas around the world, and you must navigate their stages in order to fight them. \n ")
stage_select = stage_select.lower()
if stage_select == "flash man":
    print("Now loading Flash Man stage...\n")
    time.sleep(4.1)
>>>>>>> origin/niobium:src/megaman2/megaman2.py
