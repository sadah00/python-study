# Create a file called mydstask.py and attempt the below questions:
my_ds = [23,"Jane" , (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
# 1. Print KES
print(my_ds[3][2]["currency"])
# 2. Print 560
print(my_ds[2])
# 3. Print Maths
print(my_ds[3][1])
# 4. In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"]=90
print(my_ds)
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
x=my_ds[4]
y=str(x)
print(type(y))
y=y[::-1]
print(y)
#      Hint: Strings can be reversed using [::]
# 6. Change the name “John” to “Jane” . 
z=my_ds[5]
z=list(z)
z[1]="Jane"
z=tuple(z)
print(z)
# You can research or discuss to find the solutions above.
#         https://realpython.com/quizzes/pybasics-tuples-lists-dicts/ 

