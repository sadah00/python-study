def triangle_area(height,base):
    area=height*base*0.5
    return area

x=int(input("Enter height: "))
y=int(input("Enter base: "))

xy=triangle_area(x,y)
print(xy)

#create a function that checks if a number is even or odd number

def check_number(x):
    if x%2==0:
        res="Even number"
    else:
        res="Odd number"
    return res
z=check_number(65)
print(z)

# create a function to calculate the area of a rectangle
def rectangle_area(length,width):
    area=length*width
    print(area)

rectangle_area(30,12)

# create a function that displays the largest number among 3 numbers
def largest_number(num,num1,num2):
    if num>num1 and num>num2:
        results=num
    elif num1>num and num1>num2:
        results=num1
    else:
        results=num2
    return f"The largest number is {results}"

num=input("Enter number: ")
num=int(num)
num1=input("Enter number: ")
num1=int(num1)
num2=input("Enter number: ")
num2=int(num2)

result=largest_number(num,num1,num2)
print(result)
    
    