class Person:

	def __init__(self):
	    self.__name = ''
	    self.__address = ''
	    self.__phone = ''
	    self.__email = ''
	
	def setName(self, n):
	    self.__name = n
	
	def getName(self):
		return self.__name

	def __str__(self):
		return self.__name + self.__address + self.__phone + self.__email
		

carly = Person()
carly.setName("Carly")
print(carly)
print(ord('A'))
