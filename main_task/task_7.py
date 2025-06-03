# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.

marks=input('Enter marks: ')
marks=int(marks)
if marks>79:
    print("A")
elif marks>=60:
    print("B")
elif marks>49:
    print("C")
elif marks>40:
    print("D")
else:
    print("E")