import time
import random
print("Now running battle_template version 1.0.0....")
time.sleep(2)
print("Please standby:")
time.sleep(2)
enemy_dict = ["coolguy", "ChuckBot"]
print(f"You are now battling the enemy")
while True:
    Enemy_HP = 300
    Player_HP = 500
    if Enemy_HP <= 0:
        print("You have won.")
    elif Enemy_HP > 0:
        print("The battle ensues...")
        Enemy_attack = random.randint(0,200)
        print(f"The enemy damaged you with \n {Enemy_attack} damage!")
        Player_HP = Player_HP - Enemy_HP
    if Player_HP <= 0:
        print("YOU DIED")
    elif Enemy_HP > 0 and Player_HP > 0:
        player_command = input("what will you do? \n type i for info about what you can do.").lower()
        if player_command == "i":
            print("Attack with typing in a, heal slightly with h, \n defend with d, \n and run away with r. \n You will get hurt if you run away, though")
            time.sleep(4)
        elif player_command == "a":
            player_attack = random.randint(0,100)
            print(f"You attacked the enemy! You dealt {player_attack} damage.")
            time.sleep(4)
        elif player_command == "r":
            Player_HP = random.randint (0,500) / 2
            print("You shouldn't have run away.\n")
            time.sleep(4)
            print("Don't give up.")
            break
        elif player_command == "d":
            Enemy_attack == (1/random.randint(1,4))  * Enemy_attack
            print(f"You defended. Damaged reduced.") 
            time.sleep(4)                          


