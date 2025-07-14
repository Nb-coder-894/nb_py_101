# This the test zone for the features such as save, load, run, and to add things to the player data, along with the original battle experience.
# Now trying to test the dictionary player data add function.
player_data = {
    "Weapons" : ["Mega_buster"]
}
print("Now running player data add mode.")
no = int(input("nonumberger1"))
if no == 1:
    player_data["Weapons"].append("Quick_Boomerang")
    print(player_data["Weapons"])
# Note to future self. When calling stuff from a dictionary, always use square brackets.
# Alright, so to add stuff to the list, you have to basically append the called list (see line 9) outside of the dictionary calling. That's gud to know.