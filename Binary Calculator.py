# Purpose: Binary Calculator (Addition - Subtraction - One's Complement - Two's Complement).
# ========================================================================================================================================== #

def check_bin(num):                                                  # Check the number is binary or not?
    bin_characters = "01"
    for x in num:
        if x not in bin_characters:
            return False
    return True

def length_check(num, num2):                                        # Check Length
    if len(num) > len(num2):
        num2 = '0'*(len(num) - len(num2)) + num2
    elif len(num) < len(num2):
        num = '0'*(len(num2) - len(num)) + num
    return num, num2

def one_complement(num):                                             # One's Complement
    result = ""
    for x in num:
        if x == '0':
            print(result+"1", end="")
        if x == "1":
            print(result+"0", end="")
    print(result)
    
def two_complement(num):                                           # Two's Complement
    check = len(num)
    counter_two = check - 1
    two_s_comple = list(num)
    while counter_two >= 0:
        if two_s_comple[counter_two] == '1':
            counter_two -= 1
            break
        else :
            counter_two -= 1
    while counter_two >= 0:
        if two_s_comple[counter_two] == '0':
            two_s_comple[counter_two] = '1'
        else:
            two_s_comple[counter_two] = '0'
        counter_two -= 1
    counter = 0
    result = ''
    while counter < check:
        result = result + two_s_comple[counter]
        counter += 1
    return result
    
def add_bin(num ,num2):                                              # Addition
    num , num2 = length_check(num, num2)
    counter = -1
    binary_sum = ''
    carry = '0'
    if len(num) >= len(num2):
        while counter >= -len(num2):
            bit_sum = int(num[counter]) + int(num2[counter]) + int(carry)
            if bit_sum == 0:
                carry='0'
                binary_sum = '0' + binary_sum
            elif bit_sum == 1:
                carry='0'
                binary_sum = '1' + binary_sum
            elif bit_sum == 2:
                binary_sum = '0' + binary_sum
                carry = '1'
            else:
                binary_sum = '1' + binary_sum
                carry = '1'
            counter -= 1
        if carry == '1':
            binary_sum = '1' + binary_sum
        print(binary_sum)

def sub_bin(num , num2):                                             # Subtraction
        num , num2 = length_check (num, num2)
        num2 = two_complement(num2) 
        counter = -1
        binary_diff = ''
        carry = '0'
        while counter >= -len(num):
            bit_sum = int(num[counter]) + int(num2[counter]) + int(carry)
            if bit_sum == 0:
                binary_diff = '0' + binary_diff
                carry = '0'
            elif bit_sum == 1:
                binary_diff = '1' + binary_diff
                carry = '0'
            elif bit_sum == 2:
                binary_diff = '0' + binary_diff
                carry = '1'
            else:
                binary_diff = '1' + binary_diff
                carry = '1'
            counter -= 1
        print(binary_diff)

#### Main Program ####

while True:
    print("** Binary Calculator **")
    print("A) Insert new numbers.")
    print("B) Exit.")
    choice_menu1 = str(input("Enter your choice (A/B): ").upper().strip())

# If choice is A (Insert new numbers):
    if choice_menu1 == "A":
        num = input("Please insert the number: ")                                    # Input the first number from the user.
        while check_bin(num) == True:
            print("** Please select the operation: **")
            print("A) Compute One's Complement.\nB) Compute Two's Complement.\nC) Addition.\nD) Subtraction.")
            choice_menu2 = str(input("Enter your choice (A/B/C/D): ").strip().upper())
        
        # If choice is A (One's Complement):
            if choice_menu2 == "A":
                print('The final result = ', end=''), one_complement(num)
                print()  
                break
        
        # If choice is B (Two's Complement):
            elif choice_menu2 == "B":
                result = two_complement(num)
                print('The final result =', result), print()
                break
            
        # If choice is C (Addition):
            elif choice_menu2 == "C":
                num2 = input("Please insert the second number: ")                    # Input the second number from the user.
                if check_bin(num2) == True:
                    print('The final result = ', end=''), add_bin(num, num2), print()
                    break
                else:
                    print("Invalid Input.\n")
            
        # If choice is D (Subtraction):
            elif choice_menu2 == "D":
                num2 = input("Please insert the second number: ")                    # Input the second number from the user
                if check_bin(num2) == True:
                    print('The final result = ', end=''), sub_bin(num, num2), print()
                    break
                else:
                    print("Invalid Input.\n")
        
        # If choice is not (A ,B ,C or D):
            else:
                print("Please select a valid choice.\n")
        else:
            print("Invalid Input.\n")

# If choice is B (Exit):
    elif choice_menu1 == "B":
        break

# If choice is not (A or B):
    else:
        print("Please select a valid choice.\n")
