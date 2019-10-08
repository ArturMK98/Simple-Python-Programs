"""
    Student name: Artur Karolewski
    Student number: 17388976

        This program works as follows:
            - 1: The user is prompted to enter a number
            - 2: The square root of that nuber is printed out to the screen
"""

x = input("Enter a number to find its square root\n")

try:
    print("Square root of ", x, " is ", float(x) ** 0.5)
except ValueError:
    print("You have not entered a number!")