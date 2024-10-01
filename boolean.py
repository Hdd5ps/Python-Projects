'''boolean -> True of False
x = 5
if x < 10:
print("cool")

logical operators
and- combines two boolean expressions and is only true if both are true

or- combines two boolean expressions and is true if either (or both) is (are) true

not- negates a single boolean expression
	T	F
   if x < 10 and x % 2 == 0:
	print("whoo!")
whole expression is false.


logic examples
'''

x = 5

if x < 1:
  print("cool")

print('all alone')

if x == 10:
  print("not cool")  
#use indent(space) after the if or similar function to make it a part of the function and indentation should be aligned properly don't use tab and space in the same line

#Output:
#cool
#all alone
'''
boolean - True of False
	    1	    0
Variables
	flag = True
	if flag:
	do something
 
	logic operators

	x 		y		x and y		x or y		not x
	true true		true		true		false
	true False		false		true		false
	false true		false		true		True
	false false		false		false		true
 '''
#declare constant
x = 5
y = 10
z = 3.1

v1 = x < 10
v2 = y > 20
v3 = x + (y > z) # true treated as 1

print ( v1 )
print ( v2 )
print ( v3 )

print (v1 and v2)
print (v2 and v3)
print (v1 or v2 or v3)

# mathematical operations before any relational operators because mathematical has higher precedence

x = int(input("Some value: "))

if x == 4 or x == 0: # what happens if I type x == 4 or 0: it won't print anything after or the python interprets 0  as false and because there are two false the code won't print anything
  print("good value")