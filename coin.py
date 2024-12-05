import random

class Coin:
	
	def __init__(self):
		self.__value = 1
		self.__sideup = 'heads'
	
	def getSide(self):
		return self.__sideup
	
	def getValue(self):
		return self.__value
	
	def toss(self):
		val = random.randint(1,2)
		if val == 1:
			self.__sideup = 'heads'
		else:
			self.__sideup = 'tails'

