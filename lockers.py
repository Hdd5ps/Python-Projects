lockers = ['c']*151
for jump in range(2,151):
	for index in range(jump,151,jump):
		if lockers[index] == 'c':
			lockers[index] = 'o'
		else:
			lockers[index] = 'c'	
for index in range(1,151):
	if lockers[index] == 'c':
		print(index)
