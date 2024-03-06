def check_num(num):
    characters = "0123456789AaBbCcDdEeFf"
    for x in num:
        if x not in characters:
            return False
    return True

def check_dec(num):                              #Check the number is Decimal or not ?
    dec_characters = "0123456789"
    for x in num:
        if x not in dec_characters:
            return False
    return True

def dec_to_bin(num):                               #Convert the number from Decimal to binary
    if num > 1:
        dec_to_bin(num//2)
    print(num%2 ,end="")

def dec_to_oct(num):                             #Convert the number from Decimal to octal
    oct_num = [0] * 100
    i = 0
    while (num != 0):
        oct_num[i] = num % 8
        num = int(num / 8)
        i = i + 1
    for j in range(i -1, -1, -1):
        print(oct_num[j], end="")

def dec_to_hex(num):                             #Convert the number from Decimal to hexadecimal
    hex_num = ''
    if num == 0:
        print(num)
    while num > 0:
        remainder = num % 16
        if remainder == 10:    remainder = 'A'
        elif remainder == 11:  remainder = 'B'
        elif remainder == 12:  remainder = 'C'
        elif remainder == 13:  remainder = 'D'
        elif remainder == 14:  remainder = 'E'
        elif remainder == 15:  remainder = 'F'
        hex_num = str(remainder) + hex_num
        num = num // 16
    print(hex_num)

def check_bin(num):                              #Check the number is Binary or not ?
    bin_characters = "01"
    for x in num:
        if x not in bin_characters:
            return False
    return True

def bin_to_dec(num):                             #Convert the number from Binary to Decimal
    sum = 0
    z = len(num) -1
    for i in num:
        i = int(i)
        sum = sum + (i * (2**z))
        z = z -1
    print(sum)

def bin_to_oct(num):                             #Convert the number from Binary to Octal
    sum = 0
    z = len(num) -1
    for i in num:
        i = int(i)
        sum = sum + (i * (2**z))
        z = z -1
    dec_to_oct(sum) ,print()

def bin_to_hex(num):                             #Convert the number from Binary to Hexadecimal
    sum = 0
    z = len(num) -1
    for i in num:
        i = int(i)
        sum = sum + (i * (2**z))
        z = z -1
    dec_to_hex(sum)

def check_oct(num):                              #Check the number is Octal or not ?
    oct_characters = "01234567"
    for x in num:
        if x not in oct_characters:
            return False
    return True

def oct_to_dec(num):                             #Convert the number from Octal to Decimal
    sum = 0
    z = len(num) -1
    for i in num:
        i = int(i)
        sum = sum + (i * (8**z))
        z = z -1
    print(sum)

def oct_to_bin(num):                             #Convert the number from Octal to Binary
    sum = 0
    z = len(num) -1
    for i in num:
        i = int(i)
        sum = sum + (i * (8**z))
        z = z -1
    dec_to_bin(sum) ,print()

def oct_to_hex(num):                             #Convert the number from Octal to Hexadecimal
    sum = 0
    z = len(num) -1
    for i in num:
        i = int(i)
        sum = sum + (i * (8**z))
        z = z -1
    dec_to_hex(sum)

def hex_to_dec(num):                             #Convert the number from Hexadecimal to Decimal
    chk = dec_num = i = 0
    hlen = len(num) - 1
    while hlen>= 0:
        if num[hlen]>= '0' and num[hlen]<= '9':
            rem = int(num[hlen])
        elif num[hlen]>= 'A' and num[hlen]<= 'F':
            rem = ord(num[hlen]) - 55
        elif num[hlen]>= 'a' and num[hlen]<= 'f':
            rem = ord(num[hlen]) - 87
        else:
            chk = 1
            break
        dec_num = dec_num + (rem * (16 ** i))
        hlen = hlen - 1
        i = i+1
    if chk == 0:
        print(dec_num)
    else:
        print("\nInvalid Input!")

def hex_to_bin(num):                             #Convert the number from Hexadecimal to Binary
    chk = dec_num = i = 0
    hlen = len(num) - 1
    while hlen>= 0:
        if num[hlen]>='0' and num[hlen]<='9':
            rem = int(num[hlen])
        elif num[hlen]>='A' and num[hlen]<='F':
            rem = ord(num[hlen]) - 55
        elif num[hlen]>='a' and num[hlen]<='f':
            rem = ord(num[hlen]) - 87
        else:
            chk = 1
            break
        dec_num = dec_num + (rem * (16 ** i))
        hlen = hlen - 1
        i = i+1
    if chk == 0:
        dec_to_bin(dec_num) ,print()
    else:
        print("\nInvalid Input!")

def hex_to_oct(num):                             #Convert the number from Hexadecimal to Octal
    chk = dec_num = i = 0
    hlen = len(num) - 1
    while hlen>= 0:
        if num[hlen]>='0' and num[hlen]<='9':
            rem = int(num[hlen])
        elif num[hlen]>='A' and num[hlen]<='F':
            rem = ord(num[hlen]) - 55
        elif num[hlen]>='a' and num[hlen]<='f':
            rem = ord(num[hlen]) - 87
        else:
            chk = 1
            break
        dec_num = dec_num + (rem * (16 ** i))
        hlen = hlen - 1
        i = i+1
    if chk == 0:
        dec_to_oct(dec_num) ,print()
    else:
        print("\nInvalid Input!")

#### Main Program ####

while True:
    print("** Numbering System Converter **")
    print("A) Insert a new number.")
    print("B) Exit program.")
    choice_menu1 = str(input("Enter your choice (A/B): "))
#If choice_menu1 is A (Insert a new number):
    if choice_menu1 == "A" or choice_menu1 == "a":
        num = input("Please insert a number: ")                              #Input the number from the user
        while check_num(num) == True:
            print("**Please select the base you want to convert a number from:**")
            print("A) Decimal.\nB) Binary.\nC) Octal.\nD) Hexadecimal.")
            choice_menu2 = str(input("Enter your choice (A/B/C/D): "))
            
        #If choice_menu2 is A (Convert from Decimal to " "):
            if choice_menu2 == "A" or choice_menu2 == "a":
                while check_dec(num) == True:
                    print("**Please select the base you want to convert a number to:**\nA) Decimal.\nB) Binary.\nC) Octal.\nD) Hexadecimal.")
                    choice_menu3 = str(input("Enter your choice (A/B/C/D): "))
                    num = int(num)
                    if choice_menu3 == "A" or choice_menu3 == "a":
                        print('The final result=' ,num, "\n")
                        break
                    elif choice_menu3 == "B" or choice_menu3 == "b":                  #Convert the number from Decimal to Binary
                        print('The final result = ' ,end='') ,dec_to_bin(num) , print("\n")
                        break
                    elif choice_menu3 == "C" or choice_menu3 == "c":                  #Convert the number from Decimal to Octal
                        print('The final result = ' ,end='') ,dec_to_oct(num) ,print("\n")
                        break
                    elif choice_menu3 == "D" or choice_menu3 == "d":                  #Convert the number from Decimal to Hexadecimal
                        print('The final result = ' ,end='') ,dec_to_hex(num) ,print()
                        break
                    else:
                        print("Please select a valid choice.\n")
                else:
                    print("Invalid Input.\n")
                break
            
            #If choice_menu2 is B (Convert from Binary to " "):
            elif choice_menu2 == "B" or choice_menu2 == "b":
                while check_bin(num)== True:
                    print("**Please select the base you want to convert a number to:**\nA) Decimal.\nB) Binary.\nC) Octal.\nD) Hexadecimal.")
                    choice_menu3 = str(input("Enter your choice (A/B/C/D): "))
                    if choice_menu3 == "A" or choice_menu3 == "a":                    #Convert the number from Binary to Decimal
                        print('The final result = ' ,end='') ,bin_to_dec(num) , print()
                        break
                    elif choice_menu3 == "B" or choice_menu3 == "b":
                        print('The final result =' ,num) , print()
                        break
                    elif choice_menu3 == "C" or choice_menu3 == "c":                  #Convert the number from Binary to Octal
                        print('The final result = ' ,end='') ,bin_to_oct(num) , print()
                        break
                    elif choice_menu3 == "D" or choice_menu3 == "d":                  #Convert the number from Binary to Hexadecimal
                        print('The final result = ' ,end='') ,bin_to_hex(num) , print()
                        break
                    else:
                        print("Please select a valid choice\n")
                else :
                    print("Invalid Input.\n")
                break
            
            #If choice_menu2 is C (Convert from Octal to " "):
            elif choice_menu2 == "C" or choice_menu2 == "c":
                while check_oct(num) == True:
                    print("**Please select the base you want to convert a number to:**\nA) Decimal.\nB) Binary.\nC) Octal.\nD) Hexadecimal.")
                    choice_menu3 = str(input("Enter your choice (A/B/C/D): "))
                    if choice_menu3 == "A" or choice_menu3 == "a":                    #Convert the number from Octal to Decimal
                        print('The final result = ' ,end='') ,oct_to_dec(num) , print()
                        break
                    elif choice_menu3 == "B" or choice_menu3 == "b":                  #Convert the number from Octal to Binary
                        print('The final result = ' ,end='') ,oct_to_bin(num) , print()
                        break
                    elif choice_menu3 == "C" or choice_menu3 == "c":
                        print('The final result =' ,num, "\n")
                        break
                    elif choice_menu3 == "D" or choice_menu3 == "d":                  #Convert the number from Octal to Hexadecimal
                        print('The final result = ' ,end='') ,oct_to_hex(num) , print()
                        break
                    else:
                        print("Please select a valid choice,\n")
                else:
                    print("Invalid Input.\n")
                break
            
            #If choice_menu2 is D (Convert from Hexaecimal to " "):
            elif choice_menu2 == "D" or choice_menu2 == "d":
                while check_num(num) == True:
                    print("**Please select the base you want to convert a number to:**\nA) Decimal.\nB) Binary.\nC) Octal.\nD) Hexadecimal.")
                    choice_menu3 = str(input("Enter your choice (A/B/C/D): "))
                    if choice_menu3 == "A" or choice_menu3 == "a":                    #Convert the number from Hexadecimal to Decimal
                        print('The final result = ' ,end='') ,hex_to_dec(num) , print()
                        break
                    elif choice_menu3 == "B" or choice_menu3 == "b":                  #Convert the number from Hexadecimal to Binary
                        print('The final result = ' ,end='') ,hex_to_bin(num) , print()
                        break
                    elif choice_menu3 == "C" or choice_menu3 == "c":                  #Convert the number from Hexadecimal to Octal
                        print('The final result = ' ,end='') ,hex_to_oct(num) , print()
                        break
                    elif choice_menu3 == "D" or choice_menu3 == "d":
                        print('The final result =' ,num, "\n")
                        break
                    else:
                        print("Please select a valid choice.\n")
                else:
                    print("Invalid Input.\n")
                break
            
        #If choice_menu2 is not (A ,B ,C or D):    
            else:
                print("Please select a valid choice.\n")
        else:
            print("Invalid Input.\n")

#If choice_menu1 is B (Exit Program):
    elif choice_menu1 == "B" or choice_menu1 == "b":
        break

#If choice_menu1 is not (A or B):
    else:
        print("Please select a valid choice.\n")