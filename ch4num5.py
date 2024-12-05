'''
	Weird sum thing
'''
endVal = 31
mysum = 0
for numerator in range(1, endVal):
	mysum += (numerator/(endVal-numerator))

print(mysum)
