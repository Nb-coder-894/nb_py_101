import time
print("Now running Megaman2 RPG edition\n Version 1.0.0")
time.sleep(1)
print("You are megaman.\n")
time.sleep(1)
print("Now entering stage select.\n")
weapon_inventory = []
x_position = 0
y_position = 0
while True:
    weapon_inventory.append("Mega_Buster")
    stage_select = input("Which stage? Air Man, Crash Man, Heat Man, Bubble Man, Wood Man, Quick Man, Flash Man, or Metal Man?")
    stage_select = stage_select.lower()
    if stage_select == "metal man":
        print("Now loading Metal Man stage...\n Get your weapons ready...")
        time.sleep(2)
        print("Now in the starting area of Metal Man. \nTo select your weapon, type in w. \n To move, type in m. \n To jump, press j. ")
        for i in range (1,300):
            move_request = input("What will you do? Move using m? Equip weapon using w? \n Jump using J?")
            move_request = move_request.lower()
            if move_request == "w":
                print(f"Your selected weapon is {weapon_inventory}")
            elif move_request == "m":
                move_direction = input("Forward or backward? type in f or b to do that.")
                move_direction = move_direction.lower()
                if move_direction == "b" and x_position == 0:
                    print("You can't do that")
                elif move_direction == "f":
                    print("work in progress")    

   
