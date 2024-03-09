# Purpose : Subtract a Square game in python, where 2 players alternate in entering a perfect square number
#           to try to get a random number of coins to be 0, where the player that takes the last coin wins.
# ============================================================================================================================================= #

from random import randint as r

# Printing welcome screen
print('#==== Welcome to Subtract a Square Game ====#')

print('Choice:\n 1) Select number of coins manually. \n 2) Select a random number of coins.')
game_mode = input('Enter your choice: ')                                        # Selecting game mode

while game_mode not in ["1", "2"]:
    print('Please select a valid choice.\n\nChoice:\n 1) Select number of coins manually. \n 2) Select a random number of coins.')
    game_mode = input('Enter your choice: ')                                   # Selecting game mode

if game_mode == "1":
    while True:
        try:
            n_coins = int(input('Select the number of coins: '))
            break
        except ValueError:
            print("Please enter a valid number.")
elif game_mode == "2":
    n_coins = r(1, 1000)                                                # Choosing a random number of coins

print(f'\nNumber of coins = {n_coins}')

while n_coins > 0:
    while True:
        try:
            move = int(input('Player 1: Please take a square number of coins: '))    # Taking number of coins to remove
            break
        except ValueError:
            print("Please enter a valid integer number.")

    while not (move**0.5).is_integer() or move > n_coins or move <= 0:           # Checking if the input is a square number or is smaller than n_coins or negative
        print("Please enter a square number.")
        while True:
            try:
                move = int(input('Player 1: Please take a square number of coins: '))
                break
            except ValueError:
                print("Please enter a valid integer number.")
    n_coins -= move                                                   # Updating n_coins
    print(f'\nNow we have {n_coins} coins!')                          # Showing new value of n_coins

    if n_coins <= 0:                                                  # Check win
        print('Player 1 wins!')
        break

    while True:
        try:
            move = int(input('Player 2: Please take a square number of coins: '))  # Taking number of coins to remove
            break
        except ValueError:
            print("Please enter a valid integer number.")
    while not (move**0.5).is_integer() or move > n_coins or move <= 0:
        print("Please enter a square number.")
        while True:
            try:
                move = int(input('Player 2: Please take a square number of coins: '))
                break
            except ValueError:
                print("Please enter a valid integer number.")

    n_coins -= move
    print(f'\nNow we have {n_coins} coins!')

    if n_coins <= 0:
        print('Player 2 wins!')
        break
