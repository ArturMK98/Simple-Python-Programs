"""
    Student name: Artur Karolewski
    Student number: 17388976

        This program works as follows:
            - 1: The user is prompted to enter the values for a, b and c
            - 2: The program calculates two solutions
            - 3: The results are printed out to the screen
"""

# import complex math module
import cmath

# Take coefficient input from the users
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# Solve the quadratic equation ax**2 + bx + c = 0 and find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))