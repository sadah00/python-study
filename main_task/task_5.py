# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, 
# and stores them in three variables. Return the largest of the three. 
# Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

note=input('Type number: ')
note=int(note)
note1=input('Type number: ')
note1=int(note1)
note2=input('Type number: ')
note2=int(note2)
if note>note1 and note>note2:
    print(f'{note} is the largest')
elif note1>note and note1>note2:
    print(f'{note1}is the largest')
else:
    print(f'{note2} is the largest')   