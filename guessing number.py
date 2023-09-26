# task 1
# number guessing game

# import random for random numbers
from random import randint

# randint module generates the random number between the two given number
number = randint(1, 100)

# main look
print("   ┌─────────────────────────────────────────────────┐")
print("   │       WELCOME TO THE NUMBER GUESSING GAME       │")
print("   └─────────────────────────────────────────────────┘")

# player name
player_name = input("Enter your name:")

# game rules
print("\n*** GAME RULES ***")
print("- You have 10 attempts to guess a secret number between 1 and 100.")
print("- After each guess, you'll receive feedback to help you narrow down your guess.")
print("- If you guess correctly within 10 attempts, you win the game!")
print("- If not, the game will reveal the secret number, and you can choose to play again.")

print(f"  Read the rules carefully.\n")
print(f"Hello, {player_name}! I'm thinking of a number between 1 and 100. Try to guess it within 10 attempts.")
print("loading 10 attempts...\n")


# Define the game logic inside a function
def guess_numbers():
    total_attempts = 0

    # 10 attempts for the user
    while total_attempts < 10:
        guess_no = int(input('Enter your guess between (1-100):'))
        total_attempts += 1
        if guess_no > number:
            print('Too high!')

        elif guess_no < number:
            print('Too low!')

        if guess_no == number:  # if the guess is right
            print(f'Congratulations {player_name}!!')
            print(f"You guessed it right! The secret number was {number} \nYOU WON THE GAME.\n")
            break

        # for the guess below than 9
        elif total_attempts < 9 and guess_no != number:
            print("Wrong guess, try again!")
            # it shows that how many attempts left
            print(f"You have {10 - total_attempts} attempts remaining.\n")

        # for the 9 attempt and still you didn't guess
        elif total_attempts == 9:
            print(f'Wrong guess, Try to guess it {player_name}')
            print('This is the last chance to guess')
            print(f"You have {10 - total_attempts} attempt remaining.\n")

        if total_attempts == 10:  # if you used all the attempts
            print("Wrong guess")
            print("Oops! No attempt left\n")
            print(f'You have lost {player_name}!!\nGAME OVER.')
            print(f"The Right Answer was number {number}\n")


try:
    # Call the guess_numbers() function to start the game
    guess_numbers()

# exception handling
except ValueError:
    print('Invalid value! Enter an integer')

# loop to ask the User to play again or not
while True:
    replay = input("Do you want to play again? (yes/no): ").lower()

    if replay == "yes":
        number = randint(1, 100)  # Generate a new random number for the next game
        print("I'm thinking of a number between 1 and 100. Try to guess it within 10 attempts.")
        guess_numbers()

    elif replay == "no":
        print(f'Goodbye {player_name}!\nHope you enjoyed it:)')
        exit()

    else:
        print("Invalid Input!")
