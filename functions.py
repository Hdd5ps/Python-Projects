'''
	Function examples
'''
import random
'''
x = 10

def fun():
	print("called the function")


print(fun())
print(x)
print(fun)
print(print)
print(type(print))
print(type(x))
'''
#function to determine if a value is even
def isEven( value ):
	if value % 2 == 0:
		return True
	else:
		return False
#######end function
evens = 0
odds = 0
for x in range(100):
	num = int(random.random()*1000)
	print(num)
	if isEven(num):
		evens += 1
	else:
		odds += 1
#summary
print("Number of evens:", evens)
print("Number of odds:",odds)
