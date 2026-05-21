import time
import random
print("Now running battle_template version 1.0.0....")
time.sleep(2)
print("Please standby:")
time.sleep(2)
enemy_dict = ["coolguy", "ChuckBot"]
print(f"You are now battling the {enemy_dict(0)}")
while True:
    Enemy_HP = 300
    Player_HP = 500
    if Enemy_HP <= 0:
        print("You have won.")
    elif Enemy_HP > 0:
        print("The battle ensues...")
        Enemy_attack = random.randint(0,200)
        print(f"The {enemy_dict(0)} damaged you with {Enemy_attack} damage!")
        Player_HP = Player_HP - Enemy_HP
    if Player_HP <= 0:
        print()             


