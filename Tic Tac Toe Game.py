# Program: A board of 3 x 3 is displayed and player 1 takes odd numbers 1, 3, 5, 7, 9 and player 2 takes
#          even numbers 0, 2, 4, 6, 8. Players take turns to write their numbers. Odd numbers start.
#          Use each number only once. The first person to complete a line that adds up to 15 is the winner.
#          The line can have both odd and even numbers.
# ==================================================================================================================== #

arr = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]       # Shape pf the game.
p1 = [1, 3, 5, 7, 9]                                            # Player One's List.
p2 = [0, 2, 4, 6, 8]                                            # Player Two's List.
menu_row_col = [1, 2, 3]

def game():                                 # Printing the shape of the game.
    print("3| ", arr[0][0], " ", arr[0][1], " ", arr[0][2])
    print("2| ", arr[1][0], " ", arr[1][1], " ", arr[1][2])
    print("1| ", arr[2][0], " ", arr[2][1], " ", arr[2][2])
    print("_|____________")
    print(" |  1   2   3 ")

def player(text, p):
    print(f"It's Player {text}'s Turn.")
    game()                              # Printing the shape of the game.
    while True:                         # Check the input is integer.
        try:
            num = int(input(f"Player {text}, Enter Your Number in {p}: ").strip())
            if num in p:
                break
            else:
                print("Please enter a valid number in the above list !!")
        except ValueError:
            print("Please enter a valid number!")
    while True:
        try:
            row = int(input(f"Player {text}, Enter The Row: ").strip())          # Get the row and check the validity of it
            if row in menu_row_col:
                if row == 3:
                    row = 0
                elif row == 2:
                    row = 1
                elif row == 1:
                    row = 2
                col = int(input(f"Player {text}, Enter The Column: ").strip())       # Get the column and check the validity of it
                if col in menu_row_col:
                    if col == 3:
                        col = 2
                    elif col == 2:
                        col = 1
                    elif col == 1:
                        col = 0
                    if arr[row][col] == "*":
                        break
                    else:
                        print("Error, This position isn't available !!")
                else:
                    print("Please enter a valid column !!")
            else:
                print("Please enter a valid row !!")
        except ValueError:
            print("Please enter a valid number !!")
    p.remove(num)
    arr[row][col] = num
    print()

def checkDiag():                                # Check if the player won diagonally.
    global win
    win = False
    if arr[0][0] != "*" and arr[1][1] != "*" and arr[2][2] != "*":
        if arr[0][0] + arr[1][1] + arr[2][2] == 15:
            win = True
    if arr[0][2] != "*" and arr[1][1] != "*" and arr[2][0] != "*":
        if arr[0][2] + arr[1][1] + arr[2][0] == 15:
            win = True
    return win


def checkHorizontal():                          # Check if the player won horizontally.
    global win
    win = False
    if arr[0][0] != "*" and arr[0][1] != "*" and arr[0][2] != "*":                # The First Row.
        if arr[0][0] + arr[0][1] + arr[0][2] == 15:
            win = True
    elif arr[1][0] != "*" and arr[1][1] != "*" and arr[1][2] != "*":              # The Second Row.
        if arr[1][0] + arr[1][1] + arr[1][2] == 15:
            win = True
    elif arr[2][0] != "*" and arr[2][1] != "*" and arr[2][2] != "*":              # The Third Row.
        if arr[2][0] + arr[2][1] + arr[2][2] == 15:
            win = True
    return win

def checkvertical():                            # Check if the player won vertically.
    global win
    win = False
    if arr[0][0] != "*" and arr[1][0] != "*" and arr[2][0] != "*":                # The First Column.
        if arr[0][0] + arr[1][0] + arr[2][0] == 15:
            win = True
    elif arr[0][1] != "*" and arr[1][1] != "*" and arr[2][1] != "*":              # The Second Column.
        if arr[0][1] + arr[1][1] + arr[2][1] == 15:
            win = True
    elif arr[0][2] != "*" and arr[1][2] != "*" and arr[2][2] != "*":              # The Third Column.
        if arr[0][2] + arr[1][2] + arr[2][2] == 15:
            win = True
    return win

def check_win():                                        # Check if Player won or not ??
    global winner
    winner = False
    if checkDiag() or checkHorizontal() or checkvertical():
        winner = True
    return winner

def draw_game():                                    # Check if the game will be a draw or not ?
    global draw
    draw = True
    for i in arr:
        for j in i:
            if j == "*":
                draw = False

# ============================================>> Main Game <<============================================ #
print("# ======= Welcome To Tic Tac Toe Game ======= #")            # Printing a welcome message.
while True:
    player("One", p1)                               # It's Player One's Turn.
    check_win()
    draw_game()
    if winner == True:                          # Check if Player One won or not ??
        game()                                  # Printing the shape of the game.
        print("Congratulations, Player One is the winner !!")
        break
    elif draw == True:                          # Check if the game will be a draw or not ?
        print("It is a tie!")
        break

    else:
        player("Two", p2)                             # It's Player Two's Turn.
        check_win()
        draw_game()
        if winner == True:                          # Check if Player Two won or not ??
            game()                                  # Printing the shape of the game.
            print("Congratulations, Player Two is the winner !!")
            break
        elif draw == True:                          # Check if the game will be a draw or not ?
            print("It is a tie!")
            break