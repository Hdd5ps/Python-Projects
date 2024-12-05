'''
	Flow control
	CSC 1010
	Sept. 23, 2024
	
'''

x = 1

while x <= 10:
	if x == 5:
		break
	print(x)
	x = x + 1

print("after",x)

i = 1

while i < 10:
	j = i
	
	while j < 10:
		if j == i+1:
			continue
		print(i * j)
		j = j + 1
		
	i = i + 1		
		
