# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days
#  TODAY.
# Once you learn functions,revisit this and write this code inside a function.

from datetime import datetime
x=datetime.now()
print(x)
current_month=x.month
print(current_month)
current_year=x.year
print(current_year)
current_day=x.day
print(current_day)

dob=input('Enter your date of birth in the format dd/mm/yyyy: ')
dob=dob.split('/')
years=current_year-int(dob[2])
months=current_month-int(dob[1])
days=current_day-int(dob[0])

if months<0:
    years=years-1
    months=months+12
    if days<0:
        months=months-1
        days=days+30

print(f'You have {years} years {months} months {days} days')


