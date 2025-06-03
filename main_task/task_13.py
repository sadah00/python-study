# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user 
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” ,
#  if so then print  “Login is Successful” and if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

email='admin@mail.com'
password='Admin@123'
trials=3
 
for i in range(1,trials+1):
    mail=input('Enter email: ')
    word=input('Enter password: ')
    if mail==email and word==password:
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")
    tries=trials-i
    if tries>0:
        print(f'try again {tries} trials left')
    else:
        print("You have been blocked.")
