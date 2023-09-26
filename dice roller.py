# Task 2
# Dice Roller Simulator
import random

# main look
print('╔══════════════════════════════════════════╗')
print('║           DICE ROLLER SIMULATOR          ║')
print('╚══════════════════════════════════════════╝')
print('*** HELLO, WELCOME TO DICE ROLLER APPLICATION ***')

try:
    # function to roll the dice
    def roll_dice():
        print("\nRolling the dice...\n")

        # these shapes brought by the ASCII characters which we used in creating dice face
        # u25CF, u250C, u2500, u2510, u2502, u2514, u2518
        # ● ┌ ─ ┐ │ └ ┘

        # structure of each dice face
        dice_structure ={
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
        }

        dice = []
        total = 0

        # Create a list of dice rolls
        # die is singular of dice
        for die in range(num_dice):
            dice.append(random.randint(1, 6))

        # for printing the dice horizontally
        for line in range(5):
            for die in dice:
                print(dice_structure.get(die)[line], end="")
            print()

        # Calculate and display the total of dice rolls
        for die in dice:
            total += die
        print(f"Score of dice rolls: {total}")
        print("\nDone Rolling! \nTHANK YOU FOR TRYING IT OUT!!\n")


    # Ask the user how many dice to roll
    num_dice = int(input("How many dice would you like to roll? "))

    roll_dice()

    # loop to ask the user to play again or not
    while True:
        roll_again = input("Do you want to roll again? (Y/N)").lower()

        if roll_again == 'y':
            num_dice = int(input("How many dice would you like to roll? "))
            roll_dice()

        elif roll_again == 'n':
            print("Thank you for rolling the dice! \nHope you like it.")
            break

        else:
            print('Invalid Input! Please input "Y" or "N"')
            continue

# exception handling
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()
