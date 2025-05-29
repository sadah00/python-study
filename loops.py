fruits=["apple","banana","oranges","melon"]
for i in fruits:
    print(i)

numbers=list(range(1,101))
print(numbers)

# iterate through numbers from 20 to 40
# display even numbers
number=list(range(20,41))

for num in number:
    if num % 2 == 0:
        print(num)

# display odd numbers from 100 to 200
odd=list(range(100,201))
for x in odd:
    if x%2!=0:
        print(x)

# for i in range(100,200):
#     if i%2!=0:
#         print(i)

# store odd numbers from 100 to 200 in a list
odd_numbers=[]
for i in range(100,200):
    if i%2!=0:
        odd_numbers.append(i)
print(odd_numbers)
# store even numbers from 100 to 200 in a list
even=[]
numbers=list(range(100,200))

for num in numbers:
    if num%2==0:
        even.append(num)
print(even)

for i in range(1,50):
    if i==40:
        break
    print(i)

# ls1 = list(range(20,50))
# res = [ ]
# for i in ls1:
# 	if i == 30:
# 		break
# 	    if i%2==0:
# 		    res.append(i)
# 	    else:
# 	     "pass"
