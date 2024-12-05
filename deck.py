import card
import random

DECKSIZE = 52

class Deck:
	def reset(self):
		self.__topcard = 0
		self.__thedeck = []
		for s in card.suits:
			for f in card.faces:
				self.__thedeck.append(card.Card(f,s))
	
	def __init__(self):
		self.reset()

	def deal(self):
		if self.__topcard < DECKSIZE:
			temp = self.__thedeck[self.__topcard]
			self.__topcard += 1
			return temp
		else:
			print("The deck is empty!")
			
	def __str__(self):
		deckstr = ''
		for card in self.__thedeck:
			deckstr += str(card) + '\n'
		return deckstr

	def shuffle(self):
		#random.shuffle(self.__thedeck)
		for x in range(5000):
			s1 = random.randrange(DECKSIZE)
			s2 = random.randrange(DECKSIZE)
			temp = self.__thedeck[s1]
			self.__thedeck[s1] = self.__thedeck[s2]
			self.__thedeck[s2] = temp
