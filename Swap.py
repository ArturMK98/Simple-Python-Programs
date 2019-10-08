"""
    Student name: Artur Karolewski
    Student number: 17388976

        This program works as follows:
            - 1: The user is prompted to enter two numbers
            - 2: The program swaps the values stored in the two variables
            - 3: The result is printed out to the screen
"""

# Take input from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))