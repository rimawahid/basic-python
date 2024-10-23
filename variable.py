# Variable = String, integer, float, boolean

#String
first_name = "Kutu"
print(f"Hi {first_name}")

#Integer
age = 25
print(f"Your are {age} years old")

#float
price= 10.99
print(f"The price is {price}")

#Boolean
is_student = True
print(f"are u a student? {is_student}")

if is_student:
    print("You are student")
else:
    print("Your are not a student")


#Typecasting = the process of converting a variable from one data type to another type
#                str(), int(), float(), bool()

name = "Kutu"
age = 4
gpa = 3.2
is_student = True

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

# input() = A function that prompts the user to enter data
#            Returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

print(f"Hello {name}!")
print(f"You are {age} years old")

#Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(area)