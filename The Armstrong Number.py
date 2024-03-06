# Program: check whether a given number is an Armstrong number or not. A positive integer of 3 digits is
#           called an Armstrong number if the sum of the cubes of individual digits of the number is equal to
#           that number itself. For example, the sum of cubes of individual digits of
#           the number 153 is 1* 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 = 153. Hence, number 153 is an Armstrong number.
# ==================================================================================================================== #

print("# ========== Welcome To The Program ========== #")
print("# =========== The Armstrong Number =========== #")
while True:
    # Set the menu
    print("Choose:\n 1) Enter New Number.\n 2) Back To Menu.")
    choice_menu = str(input("Enter Your Choice: ").strip())
    if choice_menu == "1":
        # Check if the input is an integer number
        while True:
            try:
                num = int(input("Enter the positive integer number you want to check: "))
                break
            except ValueError:
                print("Please enter a valid integer number.")
        # Check that the integer is a positive integer
        while num < 1:
            print("Please enter a valid positive integer number.")
            while True:
                try:
                    num = int(input("Enter the positive integer number you want to check: "))
                    break
                except ValueError:
                    print("Please enter a valid positive integer number.")
        # Convert the integer number into string to loop on it
        num = str(num)
        length = len(num)                   # Set the variables length and sum
        sum = 0
        for i in num:                       # Loop on every index in num and turn it into integer and multiply it with the length and add this to sum
            sum += int(i) ** length
        num = int(num)
        # Check if the num is Armstrong or not
        if sum == num:
            print("The given number is an Armstrong number")
        else:
            print("The given number is not an Armstrong number")
    elif choice_menu == "2":                # Back to the menu
        break
    else:                                   # Invalid choice
        print("Please enter a valid choice.\n")