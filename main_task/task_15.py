# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable.
def calculate_gross_salary(basic_salary,benefits):
    gross_salary=basic_salary+benefits
    return gross_salary

basic_salary=float(input("Enter basic salary: "))
benefits=float(input("Enter benefits: "))

grossSalary=calculate_gross_salary(basic_salary,benefits)

print(grossSalary)

# function to calculate NHIF
def calculate_nhif(gross):
    if gross<=5999:
        nhif=150
    elif gross>=6000 and gross<7999:
        nhif=300
    elif gross>=8000 and gross<=11999:
        nhif=400
    elif gross>=12000 and gross<=14999:
        nhif=500
    elif gross>=15000 and gross<=19999:
        nhif=600
    elif gross>=20000 and gross<=24999:
        nhif=750
    elif gross>=25000 and gross<=29999:
        nhif=850
    elif gross>=30000 and gross<=34999:
        nhif=900
    elif gross>=35000 and gross<=39999:
        nhif=950
    elif gross>=40000 and gross<=44999:
        nhif=1000
    elif gross>=45000 and gross<=49999:
        nhif=1100
    elif gross>=50000 and gross<=59999:
        nhif=1200
    elif gross>=60000 and gross<=69999:
        nhif=1300
    elif gross>=70000 and gross<=79999:
        nhif=1400
    elif gross>=80000 and gross<=89999:
        nhif=1500
    elif gross>=90000 and gross<=99999:
        nhif=1600
    else:
        nhif=1700
    return nhif

# NHIF calculation and print
NHIF=calculate_nhif(grossSalary)
print("NHIF deduction:", NHIF)

# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. 
# BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
# Write a normal program but use functions if you feel comfortable.
def calculate_nssf(gross):
    if gross < 18000:
        nssf = 0.06 * gross
    else:
        nssf = 0.06 * 18000 
    return nssf

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
# Write a normal program but use functions if you feel comfortable.
def calculate_nhdf(gross):
    nhdf = gross * 0.015
    return nhdf

# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
# Write a normal program but use functions if you feel comfortable.


# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
# Write a normal program but use functions if you feel comfortable.

# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
# Write a normal program but use functions if you feel comfortable.
def calculate_nssf(gross):
    if gross < 18000:
        nssf = 0.06 * gross
    else:
        nssf = 0.06 * 18000 
    return nssf

def calculate_nhdf(gross):
    nhdf = gross * 0.015
    return nhdf

def calculate_taxable_income(gross, nssf, nhdf, nhif):
    taxable_income = gross - (nssf + nhdf + nhif)
    return taxable_income
