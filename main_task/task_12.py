# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.
# Once you learn functions,revisit this and write this code inside a function.

digit=input("enter number: ")
digit=int(digit)
digit1=input("enter number: ")
digit1=int(digit1)
digit2=input("enter number: ")
digit2=int(digit2)
digit3=input("enter number: ")
digit3=int(digit3)
if digit>digit1 and digit>digit2 and digit>digit3:
    print(f"{digit} is the greater number")
elif digit1>digit and digit1>digit2 and digit1>digit3:
    print(f"{digit1} is the greater number")
elif digit2>digit and digit2>digit1 and digit2>digit3:
    print(f"{digit2} is the greater number")
elif digit3>digit and digit3>digit1 and digit3>digit2:
    print(f"{digit3} is the greater number")


