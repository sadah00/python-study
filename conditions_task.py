#Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
num1=input("enter digit: ")
num1=int(num1)
num2=input("enter digit: ")
num2=int(num2)
num3=input("enter digit: ")
num3=int(num3)
if num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3: 
    print(f"{num2} is the largest number")
else :
    print(f"{num3} is the largest numbers")
# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=input("enter temp: ")
temp=int(temp)
if temp>30:
    print("The temperature is too high")
elif temp>15:
    print("Normal temperature")
else :
    print("Cold temperature")
# # 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met",
#  otherwise print "Conditions not met"
x=35
x=int(x)
y=780
y=int(y)
if x>=10 and x<=20 and y>100:
    print("Conditions met")
else:
    print("Conditions not met")
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". 
# If it is, print "Access   granted", otherwise print "Access denied"
password=input('enter password: ')
if password=="secret123":
    print("access granted")
else:
    print("access denied")
# 5. Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. If both conditions are true, 
# print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=80
student_score=int(student_score)
attendance=100
attendance=int(attendance)
if student_score>90 and attendance>80:
     print("Excellent student")
else:
    print("Good score, but attendance needs improvement")
#          Attempt the questions in the link below
# https://realpython.com/quizzes/python-conditional-statements/

