# # # write a program that takes users age as input
# # # if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# # # if they dont have a drivers license print you are not eligible to drive
# # # otherwise you are too young to drive
age=input("enter age: ")
age=int(age)
if age>=18:
    license=input("Do you have a drivers licence yes/no? ").lower()
    if license=="yes":
        print("you are eligible to drive")
    else: 
        print("you are not eligible to drive")
else:
    print("you are too young to drive")
# # #.# Write a program that:
# # # = > Takes the user's credit score and annual income as input.
# # # =>If the credit score is above 700, check if the income is above 50,000:
# # # =>If both conditions are met, print "Loan approved."
# # # =>If only the credit score is high, print "Income requirement not met."
# # # =>If the credit score is below 700, print "Credit score too low."
credit_score=input("credit score: ")
credit_score=int(credit_score)
annual_income=input("annual income: ")
annual_income=int(annual_income)
if credit_score>700:
    if annual_income>50000:
        print("loan approved")
    else:
        print ("Income requirement not met.")
else:
    print ("Credit score too low.")

# # # Write a program that:
# # # Takes a transaction amount and account type ("Standard" or "Premium") as input.
# # # If the account type is "Standard":
# # # Check if the amount is above 500:
# # # If it is, print "Transaction exceeds the limit for Standard accounts."
# # # If not, print "Transaction approved."
# # # If the account type is "Premium":
# # # Check if the amount is above 1,000:
# # # If it is, print "Transaction exceeds the limit for Premium accounts."
# # # If not, print "Transaction approved."
transaction_amount=input("enter amount: ")
transaction_amount=int(transaction_amount)
account_type=input("enter account type standard/premium: ").lower()
if account_type=="standard":
    if transaction_amount>500:
        print("Transaction exceeds the limit for Standard accounts")
    else :
        print("Transaction approved")
elif account_type=="premium":
    if transaction_amount>1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
# # # 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# # # If start_date comes before end_date, print "Valid period",
# # # If start_date is after end_date, print "Invalid period".
# # # If both dates are the same, print "One-day period".

start_date ='2024-01-01'
end_date = '2024-12-31'
if start_date<end_date:
    print("Valid period")
elif  start_date>end_date:
    print("Invaild period")
elif start_date==end_date:
     print("One-day period")

# # # 2.Given two strings str1 and str2, write a conditional statement that checks:
# # # If str1 is longer than str2, print "str1 is longer".
# # # If str2 is longer than str1, print "str2 is longer".
# # # If both have equal length, print "Both are of equal length".
str1="stringy"
str2="stone"
if len(str1)>len(str2):
    print(f"{str1} is longer")
elif len(str2)>len(str1):
    print(f"{str2} is longer")
else:
    print("Both are of equal length")
# # # 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# # Prints "Access Granted" if user_id is in valid_ids.
# # Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105
if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")
# # 4.Given a variable value that could be of any type, write a conditional statement that:
# # Prints "String Detected" if value is a string.
# # Prints "Integer Detected" if value is an integer.
# # Prints "Unknown Type" for any other type.
value="kutt"
if type(value)==str:
    print("String Detected")
elif type(value)==int:
    print("Integer Detected")
else :
    print("Unknown Type")
# # 5.Given x = 7 and y = 14, write nested conditional statements that print:
# # "x and y are both even" if both x and y are even numbers.
# # "Only y is even" if only y is even.
# # "Neither x nor y are even" if both are odd.
x=7
y=14
if x % 2==0:
    if y % 2==0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    if y % 2==0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")







