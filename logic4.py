'''more logic examples'''

x = 5
y = 6
z = 10

print ( x < y )
print ( x * 2 <= z)
print ( x + y < z or z > 5 )

x = int(input())

if  x < y:
	z = int(input())
	if z > y:
		print ( "z is biggest?" )
	else:
		print ( "y is biggest?" )
else:
	print( "x is biggest?" )
	
print("after if/else", z)
