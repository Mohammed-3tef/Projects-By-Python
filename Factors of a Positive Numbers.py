# Program: Finding all the factors of a +ve integer. For example,
#           in the case of the integer 12, your algorithm should report the values 1, 2, 3, 4, 6, and 12
# =============================================================================================================== #

print("# ========== Welcome To The Program ========== #")
print('# ======= Factors Of A Positive Number ======= #')
while True:
    # Set the menu
    print('Choose:')
    print(' 1) Enter A New Number.\n'
          ' 2) Back To Menu.')
    choice_menu = str(input('Enter Your Choice: ').strip())
    if choice_menu == '1':
        factors = []                        # Set a variable factors.
        while 1 == 1:
            try:                            # Check the validity of the integer number.
                num = int(input('Enter the positive integer number to know its factors: '))
                while num <= 0:                   # Check the integer number is positive.
                    print("Please enter a valid positive integer number.\n")
                    num = int(input('Enter the positive integer number to know its factors: '))
                break
            except ValueError:
                print("Please enter a valid positive integer number.\n")

        for i in range(1, num + 1):              # Loop on numbers from 1 to num to know the factors of num.
            if num / i == num // i:              # Check if (num/i) is an integer number and add this to factor list.
                factors.append(i)
        print(factors)                           # At end print factor list to the input number.
        print()
    elif choice_menu == '2':                     # Back to the menu.
        break
    else:                                        # Invalid choice.
        print("Please enter a valid choice.\n")