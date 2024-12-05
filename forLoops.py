'''For loop examples
'''
'''
for x in [1, 2, 3]:
	print(x)
	
print(range(5))

x = int(input("Enter a start: "))
y = int(input("Enter the end: "))
st = int(input("Enter the step: "))

if st < 1:
	fixed = y - 1
else:
	fixed = y + 1

for z in range(x,fixed,st):
	print(z,end=' ')
print()
print("hey there")
'''

numLines = int(input("How many lines? "))

for line in range(numLines,0,-1):
	#print some spaces in front?

	#print the line
	for asts in range(line):
		print('*',end='')
	
	#advance output to next line
	print()

