import random
import sys

# Variables
skills = ["camouflage", "hunting", "sixth sense", "tracking", "healing", "weaponskill", "mindshield", "mindblast", "animal kinship", "mind over matter"]


# Functions
def t10():
    return random.randint(1, 10)


# Classes
class Player:
    def __init__(self):
        self.combat_skill = 0
        self.endurance = 0
        self.skills = []


# print("\nThis is a basic game of the first book #1 of the Lone Wolf...")
# print("Flight from the Dark\n")
# play = input("Do you want to play? ").lower()
#
# if play not in ("y", "yes"):
#     sys.exit()
#
# print("First we need to create the character\n")

player = Player()

# input("Press enter to roll the T10 to get your COMBAT SKILL")
# roll = t10()
# player.combat_skill = roll + 10
# print(f"You rolled a {roll}, your COMBAT SKILL is {player.combat_skill}")
#
# input("\nPress enter to roll the T10 to get your ENDURANCE")
# roll = t10()
# player.endurance = roll + 20
# print(f"You rolled a {roll}, your ENDURANCE is {player.endurance}")

print("Time to choose your 5 SKILLS:\n")
while len(player.skills) < 5:
    print("Choose skill:")
    for skill in skills:
        if skill not in player.skills:
            print(skill.title())
    choice = input("Choose one: ").lower()
    if choice in skills:
        player.skills.append(choice)
    else:
        print("Not a valid choice, try again.\n")

print("You have chosen the following SKILLS:")
for skill in player.skills:
    print(skill.title())
