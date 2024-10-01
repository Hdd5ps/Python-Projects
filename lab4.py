'''
Kamal Raj Timilsena
Lab 4
Broken file
#broken
float 1, 2, 3
input 1, 2, 3
if 1^2=2^2+3^2;
print 'is a right triangle
if 2^2=1^2+3^2;
print 'is a right triangle
if 3^2 = 1^2+3^2;
print 'is a right tranlge
else;
print is not a right triangle"

'''
# taking the input(sides of the right triangle) from the user.

f = float(input("Enter the first number: "))

s = float(input("Enter the second number: "))

t = float(input("Enter the third number: "))

# conditions 

if f**2 == s**2 + t**2:
    print("These are the sides of right triangle.")

elif s**2 == t**2 + f**2:
    print("These are the sides of right triangle.")

elif t**2 == f**2 + s**2:
    print(" These are the sides of right triangle.")
    
else: 
    print("These are not the sides of right triangle.")