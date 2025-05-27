a=20
b=50
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

# write a program that prints "pass" if marks are 50 or above ,otherwise print "fail"
marks=40
if marks>=50:
    print("pass")
else:
    print("fail")
# write an if-else statement that checks if the entered password is correct.
# if yes print "access granted",otherwise print "access denied".
password=input('enter password: ')
word="camptech"
if password=="camptech":
    print("access granted")
else:
    print("access denied")

# take four inputs from a user, separately. print the largest of the numbers.
# hint: detremine ehat type of data is taken as input
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


