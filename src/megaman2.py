import time
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

   
