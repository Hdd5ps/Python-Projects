'''
sept 25 2024
for variable in [val1, val2, val3, ...., valn]:
    statements         list
    .
    .
    .
    .
    less typing faster more efficient way to write loops

for x in [1, 2, 3]:
    print(x)
    range (start, end limit, step size)

    range(5) only one parameter will be treated as limit it is same as range(0, 5, 1) which is default.
    0 1 2 3 4
        range(1, 11, 2)
    1 3 5 7 9

for x in range(1, 101):
    print(x)

for t in range (10, 0, -1):
    print(t)
'''

# x = int(input("Enter a start: "))
# y = int(input("Enter a end: "))
# z = int(input("Enter a step: "))

# if z < 1:
#     fixed = y - 1

# else:
#     fixed = y + 1

# for z in range(x, fixed, z):
#     print(z, end='')
# print()
# print("hey there")


numLines = int(input("How many lines? "))
spaces = 0
stars = numLines
for line in range(numLines,0,-1):
    #top half
    #print some spaces in front?

    # print the lines
    for stars in range(line):
        print('*', end='')

#advance output to next line
    print()

#bottom half



