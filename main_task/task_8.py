# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80.
#  If the speed is less than 70, it should print “Ok”.
#  Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
#  If the driver gets more than 12 points, the function should print: “License suspended”.
# Once you learn functions,revisit this and write this code inside a function.

speed=input("Enter speed: ")
speed=int(speed)
speed_limit=70

if speed<speed_limit:
    result="OK"
else:
    demerit_points=round((speed-speed_limit)/5)
    if demerit_points>12:
        result='License suspended'
    else:
        result=f'You have {demerit_points} points'

print(result)
    
