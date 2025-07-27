import time

print("Now running Megaman version 1.0.0")
time.sleep(2.3)
print("You are Megaman. \n You were created by Dr.Light to stop the evil intentions of Dr.Wily. \n However, after you were created, Dr.Wily created 8 Robo Masters, and sent them after you. \n You must stop them, with the aid of your Mega Buster.")
time.sleep(3.4)
player_data = {"Health" : 100,
               "Weapons" : ["Mega Buster"],
               "Stages_Cleared" : [],
               "Wily_Tower_Mode" : False,

               }    
print("Now entering stage select")
time.sleep(0.001)
stage_select = input("Which stage will you chose?\n Your options are Bubble Man, Metal Man, Air Man, Crash Man,\n Flash Man, Heat Man, Quick Man, and Wood Man. \n Type in the name of the Robo Master you would like to fight. \n Oh, and please note: You cannot just go and fight them. They are in 8 different areas around the world, and you must navigate their stages in order to fight them. \n ")
stage_select = stage_select.lower()
if stage_select == "flash man":
    print("Now loading Flash Man stage...\n")
    time.sleep(4.1)
