# Purpose: 100 Game. Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# ====================================================================================================================================== #

sum = 0                                                     # Set the value of sum.

# Welcome message and display status
print('# ===== Welcome to 100 game ===== #')
print('Sum is equal to 0')

# ========================== Game playing ========================== #
while sum < 100:
    if sum < 90:
        while True:
            try:
                move = int(input("First Player: Choose a number from 1 to 10: "))
                break
            except ValueError:
                print("Please enter a valid integer number.")

        while move > 10 or move < 1:                            # Check the validity of the number
            print("Please enter a number from 1 to 10")
            while True:
                try:
                    move = int(input("First Player: Choose a number from 1 to 10: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number.")

    # Add the first player move to the sum
    sum += move

    # Display status
    print('Sum is equal to', sum)

    # Check if the second player won
    if (sum >= 90) and (sum < 100):
        print('Second Player is closed to win')
        while True:
            try:
                move = int(input(f"Second Player: Choose a number from 1 to {(100-sum)}: "))
                break
            except ValueError:
                print("Please enter a valid integer number.")

        while move > (100-sum) or move < 1:
            while True:
                try:
                    move = int(input(f"Second Player: Choose a valid number from 1 to {(100 - sum)}: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number.")

        if move == (100-sum):
            print('Second Player is the winner.')
            break

    if sum < 90:
        while True:
            try:
                move = int(input("First Player: Choose a number from 1 to 10: "))
                break
            except ValueError:
                print("Please enter a valid integer number.")
        # check the validity of the number
        while move > 10 or move < 1:
            print("Please enter a number from 1 to 10")
            while True:
                try:
                    move = int(input("First Player: Choose a number from 1 to 10: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number.")

    # Add the second player move to the sum
    sum += move

    # Display status
    print('Sum is equal to', sum)

    # Check if the first player won
    if (sum >= 90) and (sum < 100):
        print('First Player is closed to win')
        while True:
            try:
                move = int(input(f"First Player: Choose a number from 1 to {(100 - sum)}: "))
                break
            except ValueError:
                print("Please enter a valid integer number.")

        while move > (100 - sum) or move < 1:
            while True:
                try:
                    move = int(input(f"First Player: Choose a valid number from 1 to {(100 - sum)}: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number.")

        if move == (100 - sum):
            print('First Player is the winner.')
            break
