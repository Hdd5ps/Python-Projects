'''
if else statement print out only one of true or false 
if it finds true in the first and second statement it will print only first

more logic examples
'''

x = 5 
y = 6
z = 10

print(x < y)
print(x * 2 <= z)
print(x + y < z or z > 5)

if x < y:
    z = int(input(""))
    if z > y:
        print("z is biggest?")
    else:
        print("y is biggest?")
else:
    print("x is biggest?")

print("after if/else", z)