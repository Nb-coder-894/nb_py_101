import sleep
helth = 100

def battle_mode(fightsim):
    while True:
        print("The ChuckBot is here!")
        ChuckBot_hp = 300
        player_move = input("What do you want to do? Punch it or run? type in p or r to do that.").lower()
        if player_move == "p":
            print("you punched ChuckBOt.")
            ChuckBot_hp -= 20
        elif player_move == "r":
            break
            
