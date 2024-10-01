'''
Kamal Raj Timilsena

Sept 27 2024

This program reads a positive odd integer and prints an hourglass of asterisk with that number of lines.

'''

#Read input from the user

lines = int(input("Enter the number of lines: "))

#Adjust size if it is even

if lines / 2 == lines // 2:

    lines = lines + 1

#print the top half of the hourglass

stars = lines

while stars > 0:

    #calculate the number of leading spaces

    spaces = (lines - stars) // 2

    # print leading spaces

    space = 0

    while spaces > space:

        print(' ', end = '')

        space = space + 1

    #print asterisks

    space = 0

    while stars > space:

        print("*", end = '')

        space = space + 1

    # move to the next line

    print()

    # decrease the number of asterisks for the next line.

    stars = stars - 2

# Print the bottom half of the hourglass

stars = 3

while lines >= stars:

    # calculate the number of leading spaces

    spaces = (lines - stars) // 2

    # print leading spaces
  
    space = 0

    while spaces > space:

        print(' ', end = '')

        space = space + 1

    # print asterisks

    space = 0

    while stars > space:

        print('*', end = '')

        space = space + 1

    # move to the next line

    print()

    # increase the number of asterisks for the next line

    stars = stars + 2

