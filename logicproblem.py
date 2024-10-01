'''grade output'''

#ask user for a numeric grade (0 to 100)
numeric_grade = float(input("Enter the grade: "))

# output the corresponding letter grade using a 10-point scale
if 90 <= numeric_grade < 100:
    print("A")
elif 80 <= numeric_grade < 90:
    print("B")
elif 70 <= numeric_grade < 80:
    print("C")
elif 60 <= numeric_grade < 70:
    print("B")
elif numeric_grade >= 60:
    print("D")
else:
    print("F")

'''
default = executes the code in sequential order
statement is indented some amount
if expression:
    statements

else:
    statements

for repeation we use

while expression:
    statements

x = 0
while x < 5:
    print(x)
    x = x + 1
x = 10
while x > 0:
    print(x)
    x = x - 1
print("Blast off!")
10
9
8
7
6
5
4
3
2
1
Blast off!


x = 5
while x <= 100:
    print(x)
    x = x + 5
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100

'''

x = 0
while x < 10:
    print(2**x)
    x = x + 1
