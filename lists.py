fruits=['pineapples','banana','apples','mangoes','grapes']
# indexing
print(fruits[3])
# slicing
print(fruits[1:5])

my_list=[10,20,30,'python','HTML']
my_list[3]='Java'
my_list[4]='CSS'
print(my_list)
print(len(my_list))

# methods
my_list.append('python')
my_list.append('git')
x=my_list.copy()
my_list.insert(1,200)
z=56,79,'buoy'
my_list.extend(z)
my_list.remove(10)
my_list.pop(4)
my_list.reverse()
# m.sort(reverse=True)
print(my_list)
