'''Lab 11
'''

def main():
	#open the file
	try:
	   file = open("all_month.csv",encoding='utf8',mode='r')
	except:
		print("File not found. Terminating.")
		exit()
	line1 = file.readline()
	print(line1)
	for nextline in file:
		data = nextline.split(',')[:5]
		mag = float(data[4])
		if mag >= 5:
			print(mag)
main()
