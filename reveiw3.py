'''
	Test review
	Oct. 30, 2024
'''
def area():
	return length * width

def fileProcess():
	#open the file first
	infile = open('example.txt','r')
	total = 0 #variable to hold the total
	
	#priming read
	line = infile.readline()
	
	while line != '':
		val = int(line)
		total += val
		line = infile.readline()
	
	infile.close()
	
	return total

def main():
	print("Summing values in example.txt.")
	value = fileProcess()
	
	print("Sum is: ", value)

	x = float('50\n')
	print(x)
	
	if "0":
		print("cool")
	else:
		print("not cool")
		
x = 7 #global
#get width
#print(mystery(x))
y = 4 #global
print(x)
print(y)
