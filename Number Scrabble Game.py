# Purpose : Number Scrabble is played with the list of numbers between 1 and 9. Each player takes turns picking a number
#           from the list. Once a number has been picked, it cannot be picked again. If a player has picked three
#           numbers that add up to 15, that player wins the game. However, if all the numbers are used and no player
#           gets exactly 15, the game is a draw.
# =============================================================================================== #

from itertools import permutations
v = 0
check = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
game = [1, 2, 3, 4, 5, 6, 7, 8, 9]                           # The list of numbers between 1 and 9.
p1 = []                                                      # Player One's List.
p2 = []                                                      # Player Two's List.

def player(str, p):
    while True:
        print(f"It's Player {str}'s Turn")
        print(game)
        print(f"Player {str}'s Score:", p)
        x = input(f"Player {str}, Choose a number from the list above: ").strip()
        if x in check:                                       # Check if the input between 1 and 9 or not ?
            x = int(x)                                       # Convert the input from string to integer.
            if x in game:                                    # Check if the input in the game list or not ?
                game.remove(x)
                p.append(x)
                print(f"New Player {str}'s Score:", p, "\n")
                break
            else:
                print("Error, Number not available!!")
        else:
            print("Please enter a valid input.")

def check_win(p):
    global win
    win = False
    seq = permutations(p, 3)
    for i in list(seq):
        if i[0] + i[1] + i[2] == 15:
            win = True
    return win

# =======================>> Main Game <<======================= #

print(" #========>> Welcome To Number Scrabble Game <<========# ")
while v == 0:
    player('One', p1)                                   # It's Player One's Turn
    check_win(p1)                                           # Check if the Player One had won or not ?
    if win == True:
        print("Congratulations, Player One wins !!")
        v = 1
        break
    if game == []:                                          # Check if the game will be a draw or not?
        print("Draw !")
        break
    if v == 0:
        player('Two', p2)                               # It's Player Two's Turn
        check_win(p2)                                       # Check if the Player Two had won or not ?
        if win == True:
            print("Congratulations, Player Two wins !!")
            v = 1
            break
        if game == []:                                      # Check if the game will be a draw or not?
            print("Draw !")
            break
