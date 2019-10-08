"""
    Student name: Artur Karolewski
    Student number: 17388976

        This program works as follows:
            - 1: The user is prompted to enter two integers
            - 2: The sum of the two integers is printed out to the screen
"""

x = input("Enter the first integer:")
y = input("Enter the second integer:")

try:
    print(x, "+", y, " = ", int(x) + int(y))
except ValueError:
    print("You have not entered two integers!")
