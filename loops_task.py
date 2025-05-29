# Write a program that displays a numbers 1 to 50 inside a list.
digit=[]
for i in range(1,51):
    digit.append(i)
print(digit)
# From 1 above display the ones divisible by 7 or 5 inside a list.
div=[]
for i in range(1,51):
    if i%7==0 or i%5==0:
        div.append(i)
print(div)
# Find sum and average of values in the range between 10 to 40.
x=[10,20,30,40]
sum=0
for i in x:
    sum=sum+i
print(sum)
avg=sum/len(x)
print(avg)
# Put in a list the first 10 odd numbers between 10 to 50.
odd=[]
for y in range(10,51):
    if y%2!=0:
     odd.append(y)
    if len(odd)==10:
        break
print(odd)

# count=0
# for i in numbers:
#    if i%2==1:
#       odd.append(i)
#       count=count+1
#       if count==10:
#          break
# print(odd)

# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# get input
# convert to int
# create a list upto 10
# loop through list( for i in num)
# print()mult=x*y
value=input("enter value: ")
value=int(value)
seq=list(range(1,11))
for v in seq:
   multi=value*v
   print(f'{value}*{v}={multi}')
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even=[]
count=0
for z in range(1,51):
   if z%2==0:
      even.append(z)
      count=count+1
print(even)
ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
# Display the total quantity of the 3 above.
tt=0
for i in ls1:
   tt=tt+1[1]
print(tt)
# ls1 = [ ("Jay", '20'), ("M;o", '30'), ("Mya", '32') ]
# total=0
# for r in ls1:
# #    total=int(total)
#    total=total+1[1]
# print(total)
   

