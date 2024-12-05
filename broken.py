#broken
a = float(input('Side one: '))
b = float(input('Side two: '))
c = float(input('Side three: '))

if a**2 == b**2 + c**2:
	print('is a right triangle')
	
elif b**2 == a**2 + c**2:
	print('is a right triangle')
	
elif c**2 == a**2 + b**2:
	print('is a right triangle')
	
else:
	print("is not a right triangle")

