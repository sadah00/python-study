num1=1000
print(type(num1))
num2=23.46
print(type(num2))

x=99
y=5
# modulus %
q=x%y
print(q)

# floor //
a=x//y
print(a)

# ari1=input('enter digit:')
# ari1=int(ari1)
# ari2=input('enter digit:')
# ari2=int(ari2)
# sum=ari1+ari2
# print(sum)


# Questions
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
temp=round(temp)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp1 = 56.8926
tempp=round(temp1,2)
print(tempp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp2= 56.8926
ttemp=round(temp2,3)
print(ttemp)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
temp3=56.8926
temmp=str(temp3)
temp3=temmp[3:]
# result=float(temp3)
print(temp3)

temp3=temp3[0]+'.'+temp3[1:]
temp3=float(temp3)
print(temp3)

# NB: Use string  slice & concatenation, but have result as float
# temp=111.0789 to 78.9
temp=111.0789
nem=str(temp)
temp=nem[5:]
print(temp)
temp=temp[0:2]+'.'+temp[2]
# temp=f'{temp[0:2]}.{temp[2]}'
temp=float(temp)
print(temp)


# Attempt questions below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-data-types/




