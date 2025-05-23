student={
    'name':'Alex',
    'age':30,
    'email':'alex@gmail.com',
    }
print(type(student))
print(student)
# accsessing values in a dictionary
#key inside
print(student['age'])
print(student['email'])
print(student['age'])
#modify
student['age']=40
student['name']='Bruno'
print(student)
#add
student['phone']='0742670714'
student['occupation']='chef'
print(student)

student['location']={'town':'nakuru','address':1020,'street':'kimathi'}
print(student)
# display kimathi
print(student['location']['street'])
# display team player
student['skills']=['coding','team player','leadership']
print(student['skills'][1])
