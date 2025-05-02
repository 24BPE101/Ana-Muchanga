Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Add two numbers
SyntaxError: invalid syntax
# Add two numbers:
num1 = float(input("Enter the first number: "))
Enter the first number: 5
num2 = float(input("Enter thr second number: "))
Enter thr second number: 5
sum = num1 + num2
print("The sum of",num1, "and", num2, "is", sum)
The sum of 5.0 and 5.0 is 10.0

# Subtract two numbers:
num1 = float(input("Enter the first number: "))
Enter the first number: 10
num2 = float(input("Enter the second number: "))
Enter the second number: 5
difference = num1 - num2
print("The difference between", num1, "and", num2, "is", difference)
The difference between 10.0 and 5.0 is 5.0

# Multiply two numbers:
num1 = float(input("Enter the first number: "))
Enter the first number: 2
num2 = float(input("Enter the second number: "))
Enter the second number: 5
product = num1 * num2
print("The product of", num1, "and", num2, "is", product)
The product of 2.0 and 5.0 is 10.0

# Divide two numbers:
num1 = float(input("Enter the first number: "))
Enter the first number: 8
num = float(input("Enter the second number: "))
Enter the second number: 2
if num2 == 0
SyntaxError: expected ':'

num1 = float(input("Enter the first number: "))
Enter the first number: 8
num = float(input("Enter the second numbeer: "))
Enter the second numbeer: 2
quotient = num1 / num2
if num2 == 0:
    print("Error: division by zero is not allowed.")
    quotient = num1 / num2
    print("The quotient of", num1, "and", num2, "is", quotient)

    





# Add, multiply, subtract and divide two numbers:
num1 = float(input("Enter the first number: "))
Enter the first number: 20
num2 = float(input("Enter the second number: "))
Enter the second number: 4
sum = num1 + num2
product = num1 * num2
difference = num1 - num2
quotint = num1 / num2
if num2 == 0:
    quotient = "undefined"

    
print("Sum:",sum)
Sum: 24.0
print("Product:", product)
Product: 80.0
print("Difference:", difference)
Difference: 16.0
print("Quotient:", quotient)
Quotient: 1.6

# Convert hours into minutes:
hours = float(input("Enter the number of hours: "))
Enter the number of hours: 2
minutes = hours *60
print("The minutes equal to", minutes)
The minutes equal to 120.0

#Convert minutes into hours
minutes = float(input("Enter the number of minutes: "))
Enter the number of minutes: 120
hours = minutes / 60
print("The hours equal to", hours)
The hours equal to 2.0

# Convert dollar into rupees:
dollar = float(input("Enter the amount in dollar: "))
Enter the amount in dollar: 100
rupees = dollar * 48
print("The dollar is equal to", dollar)
The dollar is equal to 100.0
print("The rupees is equal to", rupees)
The rupees is equal to 4800.0

#Convert rupees into dollars:
rupees = float(input("Enter the amount of rupees: "))
Enter the amount of rupees: 4800
dollars = rupees / 48
print("The dollars is equal t", dollars)
The dollars is equal t 100.0

#Convert dollars into pounds:
dollars = float(input("Enter the amount of dollars: "))
Enter the amount of dollars: 200



# Convert grams into kilograms:
kilograms = float(input("Enter the weight in grams: "))
Enter the weight in grams: 10000
kilograms = grams / 1000
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    kilograms = grams / 1000
NameError: name 'grams' is not defined

kilograms = float(input("Enter the weight in grams: "))
Enter the weight in grams: 1000
Enter the weight in grams: 1000
SyntaxError: invalid syntax

grams = float(input("Enter the weight in grams: "))
Enter the weight in grams: 1000
kilograms = grams * 1000
print("The kilograms is equal to", kilograms)
The kilograms is equal to 1000000.0

# 12. kilograms into gramsa:
kilograms = floata(input("Enter the weight in kilograms: "))
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    kilograms = floata(input("Enter the weight in kilograms: "))
NameError: name 'floata' is not defined. Did you mean: 'float'?
kilograms = float(input("Enter the weight in kilograms: "))
Enter the weight in kilograms: 2
grams = kilograms * 1000
print("The kilograms is equal to", grams)
The kilograms is equal to 2000.0
print("The grams is equal to", grams)
The grams is equal to 2000.0

# 13. Convert bytes into KB, MB, and GB:
bytes = int(input("Enter the number of bytes: "))
Enter the number of bytes: 100
mb = bytes / 1024


bytes = int(input("Enter the number of bytes: "))
Enter the number of bytes: 100
kb = bytes / 1024
mb = kb /1024
gb = mb / 1024
print("Bytes is equal to:", bytes)
Bytes is equal to: 100
print("KB", kb)
KB 0.09765625
print("MB", mb)
MB 9.5367431640625e-05
print("GB", gb)
GB 9.313225746154785e-08

# 14. covert Celsius into Fahrenheit:
celsius = float(input("Enter the temperature in celsius: "))
Enter the temperature in celsius: 40
fahrenheit = (9/5) * celsius +32
print("Fahrenheit is equal to", fahrenheit)
Fahrenheit is equal to 104.0

# 15. Fahrenheit into celsius:
fahrenheit = float(input("Enter the temperature in fahrenheit: "))
Enter the temperature in fahrenheit: 104
celsius = (5/9) * (fahrenheit - 32)
print("Celsius is equal to", celsius)
Celsius is equal to 40.0

# 16. Calculate interest:
principal = float(input("Enter the principal amount: "))
Enter the principal amount: 2000
rate = float(input("Enter the rate of interest: "))
Enter the rate of interest: 50
time = float(input("Enter the time period: "))
Enter the time period: 8
interest = (principal * rate * time) / 100
print("The interest is", interest)
The interest is 8000.0

# 17. Area and perimeter of a square:
side = float(input("Enter the side of the square: "))
Enter the side of the square: 4
area = side * side
perimeter = 4 * side
print("Area of the square:", area)
Area of the square: 16.0
print("Perimeter of the square:", perimeter)
Perimeter of the square: 16.0

# 18. Area and perimeter of a rectangle:
lenght = float(input("Enter the lenght of the rectangle: "))
Enter the lenght of the rectangle: 8
breadth = float(input("Enter the breadth of the rectangle: "))
Enter the breadth of the rectangle: 4
ara = lenght * breadth
perimeter = 2 * (lenght + breadth)
print("Area of the rectangle:", rectangle)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print("Area of the rectangle:", rectangle)
NameError: name 'rectangle' is not defined
print("Area of the rectangle:", area)
Area of the rectangle: 16.0
print("Perimeter of the rectangle:", perimeter)
Perimeter of the rectangle: 24.0

# 19. calculate area of circle:
radius = float(input("Enter the radius of circle: "))
Enter the radius of circle: 6
area = (22/7) * radius * radius
print("Area of the circle:", area)
Area of the circle: 113.14285714285714

# 20. Area of a triangle:
base = float(input("Enter the base of the triangle: ")))
SyntaxError: unmatched ')'
base = float(input("Enter the base of the triangle: "))
Enter the base of the triangle: 7
height = float(input("Enter the height of the triangle: "))
Enter the height of the triangle: 7
area = (base * height) / 2
print("Area of the triangle:", area)
Area of the triangle: 24.5

# 21. Calculate the salary:
gross salary = float(input("Enter the gross salary: "))
SyntaxError: invalid syntax
gross-salary = float(input("Enter the gross salary: "))
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
salary = float(input("Enter the gross salary: "))
Enter the gross salary: 78000
allowances = 0.1 * salary
deductions = 0.03 * salary
net salary = salary + allowances - deductions
SyntaxError: invalid syntax
salary = salary + allowances - deductions
print("Salary:", salary)
Salary: 83460.0

# 22. calculate avarege of three subjects:
subject1 = float(input("Enter the marks of the first subject: "))
Enter the marks of the first subject: 65
subject2 = float(input("Enter the marks of the second subject: "))
Enter the marks of the second subject: 55
subject3 = float(input("Enter the marks of the third subject: "))
Enter the marks of the third subject: 45
total = subject1 + subject2 + subject3
average = total / 3
print("Total marks:", total)
Total marks: 165.0
print("Average marks:", average)
Average marks: 55.0

no. 22 belongs 23
SyntaxError: invalid syntax

>>> # 22. calculate net sales:
>>> gross_sales = float(input("Enter the gross sales: "))
Enter the gross sales: 50
>>> discount = 0.1 * gross_sales
>>> net_sales = gross_sales - discount
>>> print("Net sales:", net_sales)
Net sales: 45.0
>>> 
>>> # 24. swap two values:
>>> X = input("Enter the first: ")
Enter the first: 16
>>> y = input("Enter second: ")
Enter second: 15
>>> x, y = y, x
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    x, y = y, x
NameError: name 'x' is not defined
>>> x, y = x, y
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    x, y = x, y
NameError: name 'x' is not defined
>>> 
>>> X = input("Enter the first values: ")
Enter the first values: 10
>>> y = unput("Enter the second values: ")
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    y = unput("Enter the second values: ")
NameError: name 'unput' is not defined. Did you mean: 'input'?
>>> y = input("Enter the second values: ")
Enter the second values: 8
>>> print("After swapping:")
After swapping:
>>> print("x =", x)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    print("x =", x)
NameError: name 'x' is not defined
