import deck
import card


class BlackJack:
	def __init__(self):
		self.__playerhand = []
		self.__dealerhand = []
		self.__deck = deck.Deck()
	
	def pValue(self):
		c1face = self.__playerhand[0].getFace()
		c2face = self.__playerhand[1].getFace()
		
		c1val = card.faces.index(c1face) + 2
		c2val = card.faces.index(c2face) + 2
		
		#fix face cards and ace
		if c1val in [11,12,13]:
			c1val = 10
		if c1val == 14:
			c1val = 11
			
		if c2val in [11,12,13]:
			c2val = 10
		if c2val == 14:
			c2val = 11
		
		return c1val + c2val
		
	def dValue(self):
		c1face = self.__dealerhand[0].getFace()
		c2face = self.__dealerhand[1].getFace()
		
		c1val = card.faces.index(c1face) + 2
		c2val = card.faces.index(c2face) + 2
		
		#fix face cards and ace
		if c1val in [11,12,13]:
			c1val = 10
		if c1val == 14:
			c1val = 11
			
		if c2val in [11,12,13]:
			c2val = 10
		if c2val == 14:
			c2val = 11
		
		return c1val + c2val		
		
	
	def play(self):
		#first, shuffle the deck
		self.__deck.shuffle()
		
		#deal the cards, one to the player, one to the dealer, exactly 2 each
		crd = self.__deck.deal()
		self.__playerhand.append(crd)
		
		crd = self.__deck.deal()
		self.__dealerhand.append(crd)
			
		crd = self.__deck.deal()
		self.__playerhand.append(crd)
		
		crd = self.__deck.deal()
		self.__dealerhand.append(crd)
	

		#get the hand values so we can compare them	
		phandval = self.pValue()
		dhandval = self.dValue()
		#print the hands
		print(self.__playerhand[0],self.__playerhand[1], phandval,sep=', ')
		print(self.__dealerhand[0],self.__dealerhand[1], dhandval,sep=', ')		

		#now see who wins
		if phandval > 21: #bust!
			print("Player busted! :(")
			return
		if dhandval > 21:
			print("Dealer BUSTED! :)")
			return
		if phandval > dhandval:
			print("Player wins! :)")
		elif dhandval > phandval:
			print("Dealer wins. :(")
		else:
			print("Tie. Dealer wins. :(")
		
