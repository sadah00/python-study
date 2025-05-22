fruits=['pineapples','banana','apples',[20,30,40,[300,700]],'mangoes','grapes']
# indexing
print(fruits[3])
# slicing
print(fruits[1:5])

print(fruits[3][3][1])
print(fruits)
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

# trainees = ["John", [2, ["James","Mary"]]]
# 1. Display 2 from the list.
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])
# 2. Output James  from the list.
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][1][0])
# 3. Using a method add 56 at the end of the list.
trainees.append('56')
print(trainees)
# 4. Using a method add the name Mike between James and Mary
trainees[1][1].insert(1,'Mike')
print(trainees)
# 5. Change the value of 2 to 8
trainees[1][0]=8
print(trainees)
# 6. Remove John and Mary from the list.
trainees.remove('John')
trainees[0][1].remove('Mary')
print(trainees)
# 7. Using a function, determine the length of the list
print(len(trainees))
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-lists-tuples/viewer/


