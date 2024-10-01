'''
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''
x = 1
y = 1 #starting values

print(x)
print(y)

counter = 2 #starting after the first two

maxFib = int(input("Enter the number you want to go to: "))

while counter < maxFib:
    newVal = x + y #sum of privious 2
    x = y #update x to y
    y = newVal #update y to new value for next iteration
    print(newVal)
    counter = counter + 1