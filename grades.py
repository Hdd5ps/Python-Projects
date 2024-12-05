'''grade output'''

# ask user for a numeric grade (0 to 100)
numeric_value = float( input("Enter the grade: ") )

# output the corresponding letter grade using a 10-point scale

if numeric_value >= 90:
	print("A")
elif numeric_value >= 80:
	print("B")
elif numeric_value >= 70:
	print("C")
elif numeric_value >= 60:
	print("D")
else:
	print("F")
