"""
    Student name: Artur Karolewski
    Student number: 17388976

        This program works as follows:
            - 1: The user is prompted to enter the three sides of a triangle
            - 2: The program calculates the area of the triangle
            - 3: The result is printed out to the screen
"""
# taking float inputs(base or height) from the user
base = float(input('Enter base: '))
height = float(input('Enter height: '))

# calculate the area
area = ((base * 0.5) * height)
print('The area of the triangle is %0.2f' %area)
