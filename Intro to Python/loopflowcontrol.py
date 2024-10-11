'''
Sept. 23, 2024

control variable
while expression:
    statements
    update statement

if false then after the loop;
 
2 mechanisms of flow control;

-> Stop execution of a loop early by using the break statement.
    x = 1
    while x < 10:
        if x % 5 == 0
            break   (stops the if statement after the condition is met)
        print(x)
        x = x + 1

    Output= 1 
            2
            3
            4
    Operating system is constantly running a loop and it breaks when it finds a command.

-> restart at the expression by using the continue statement (infinite loop is putted instead of break w/o being careful)

x = 1
    while x < 10:
        if x % 5 == 0
            x = x + 1
            continue
        print(x)
        
    Output= 1 
            2
            3
            4
            6
            7
            8
            9

'''

x = 1
while x <= 10:
    if x == 5:
        x = x + 1
        continue
    print(x)
    x = x + 1

print("after", x)

x = 1
while x <= 10:
    if x == 5:
        x = x + 1
        break
    print(x)
    x = x + 1

print("after", x)

i = 1

while i < 10:
    j = i
    while j < 10:
        if j == i + 1:
            break
        print(i*j)
        j = j + 1
    i = i + 1

print("after", x)

i = 1

while i < 10:
    j = i
    while j < 10:
        if j == i + 1:
            continue
        print(i*j)
        j = j + 1
    i = i + 1