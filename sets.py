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
