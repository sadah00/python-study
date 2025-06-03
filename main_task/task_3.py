# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal.
#  Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. 
# Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

phone=input('Enter phone number: ')
# if phone[0:4]=='+254' and len(phone)==13:
if phone.startswith('+254') and len(phone)==13:
    valid=phone
elif phone.startswith('07') and len(phone)==10:
    valid='+254'+phone[1:]
elif phone.startswith('7') and len(phone)==9:
    valid='+254'+phone
elif phone.startswith('254') and len(phone)==12:
    valid='+'+phone
elif phone.startswith('01') and len(phone)==10:
    valid='+254'+phone[1:]
elif phone.startswith('1') and len(phone)==9:
    valid='+254'+phone
    print(f'{valid} is a valid phone number')
    
else:
    print("Invalid phone number")
