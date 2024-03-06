# Program: The German mathematician Leibniz (1646–1716) discovered the rather remarkable fact that
#           the mathematical constant PI can be computed.
#           The formula represents an infinite series; each fraction represents a term in that series.
#           If you start with 1, subtract one-third, add one-fifth, and so on, for each of the odd integers, you
#           get a number that gets closer and closer to the value of PI/4 as you go along. Then we can get PI.
# =============================================================================================================== #

print("# ========== Welcome To The Program ========== #")
print("# ===== The German Mathematician Leibniz ===== #")
while True:
    # Set the menu
    print("Choose:\n 1) Enter New Number.\n 2) Back To Menu.")
    choice_menu = str(input("Enter Your Choice: ").strip())
    if choice_menu == "1":
        i = j = 1                           # Set variables i, j and res
        res = 0
        print()
        while True:                         # Check the validity of the integer number
            try:
                num = int(input("Enter A Number: "))
                if num >= 1:
                    break
                else:
                    print("Please enter a valid positive number.")
            except ValueError:
                print("Please enter a valid integer number.")
        while j <= num:                         # Loop times equal to num to get (Pi/4)
            if j % 2 != 0:
                res = res + (1 / i)             # If j is a multiple of 2 adding (1/i) to res
            else:
                res = res - (1 / i)             # If j is not a multiple of 2 subtracting (1/i) to res
            i += 2
            j += 1
        print("The result =", res * 4, "\n")    # Multiply res with 4 to get Pi
    elif choice_menu == "2":                    # Exit Program
        break
    else:                                       # Invalid choice
        print("Please enter a valid choice.\n")