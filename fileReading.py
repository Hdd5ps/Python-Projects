'''File input example
	CSC 1010
	Oct. 26, 2024
'''

def main():
	#open up a file for reading
	infile = open('example.txt','r')
	'''	
	#read the entire file into a single variable
	contents = infile.read()
	print(contents)
	'''
	'''
	more = infile.readline()
	more = more.rstrip()
	print(more)
	
	second = infile.readline()
	print (second)
	'''
	'''
	lines = infile.readlines()
	print(lines) #list of lines
	'''
	infile.close()
	
	outfile = open("newfile.txt",'w')
	for x in range(10):
		outfile.write( str(x)+'\n' )
	outfile.close()
	
main() #call the main function
