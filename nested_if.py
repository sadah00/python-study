# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
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
#.# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."
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
    


