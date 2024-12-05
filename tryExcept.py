'''
	Python try/except examples
'''
def getValue():
	val = int(input("Enter an integer "))
	if val < 0 or val > 5:
		raise ValueError("only 1 - 5 allowed")
	return val
	
def main():
	#code here
	while True:
		try:
			value = getValue()
			number = 10 / value
			print(number)
			
			fp = open("example.txt",'r')
			break
		
		except FileNotFoundError:
			print("File not found on system. Check file name?")
		
		except ValueError as err:
			print("Expected an integer between 1 and 5.")
			print(err)
		
		except ZeroDivisionError:
			print("Tried to divide by zero.")

		except:
			print("Something bad happened.")
			print(err)

		finally:
			print("After the try/except stuff.")
		
main() #call main to start the program
'''	
		except FileNotFoundError:
			print("File not found on system. Check file name?")
		
		except ValueError as err:
			print("Expected an integer between 1 and 5.")
			print(err)
		
		except ZeroDivisionError:
			print("Tried to divide by zero.")
'''
