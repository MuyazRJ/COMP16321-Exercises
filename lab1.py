#Create a program that will ask the user for two numbers and then show the sum, product, ratio, modulus and exponentiation.

from cmath import pi
from math import gcd
from tkinter import N


number1 = input("Enter number one: ")
number2 = input("Enter number two: ")

print("Sum of " + number1, "and", number2, "is", str((int(number1) + int(number2))))
print("Product of " + number1, "and", number2, "is", str((int(number1) * int(number2))))
print("Ratio is",  (str(int(int(number1) / gcd(int(number1), int(number2))))) + ":" + (str(int(int(number2) / gcd(int(number1), int(number2))))))
print("Modulo of " + number1, "and", number2, "is", str((int(number1) % int(number2))))
print("Exponentation of " + number1, "^", number2, "is", str((int(number1) ** int(number2))))

#Create a program that asks the user for a temperature in degrees Celsius and display the conversion in Fahrenheit.

celsius = float(input("Enter the temperature in degrees Celsius: "))
print("Temperature in Fahrenheit is " + str(celsius * 1.8 + 32))

#Create a program that displays the area and the circumference of a circle given the radius.

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle is", str((pi * radius**2)), "Circumference of the circle is", str((2 * pi * radius)))

#Create a program that displays the surface area of a sphere given the radius.

radius = float(input("Enter the radius of the sphere: "))
print("Surface area of the sphere is ", str(4 * pi * radius**2))

#Create a program that displays the surface area of a cylinder given the height and the radius.

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
print("Surface area of the cylinder is ", str(2 * (pi * radius * height + pi * radius ** 2)))

#Create a program that asks the user for their first name and then their surname. The program should then display the person’s initials.

first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Your initials are: " + (first[0] + last[0]).upper())

#Create a program that asks the user for their age, the program should output false if the person is less than 18 years old and true if the person is greater than 17 years old (do use a conditional if statement).

age = int(input("Enter your age: "))
if age >= 18:
    print(True)
else:
    print(False)