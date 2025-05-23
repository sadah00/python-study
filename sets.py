numbers={10,20,30,40,50,10,20}
print(type(numbers))
print(numbers)
numbers.add(1000)
print(numbers)

days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)
# Remove friday and sunday from the set using methods.
days.remove("friday")
print(days)
days.remove("sunday")
print(days)
# Add them back to the set
days.add("friday")
print(days)
days.add("sunday")
print(days)

# differene
x={1,2,3,4,5,6,7}
y={5,6,7,8,9,10}
# z=x-y
z=x.difference(y)
print(z)
z=x.union(y)
print(z)
z=x.symmetric_difference(y)
print(z)
z=x.intersection(y)
print(z)