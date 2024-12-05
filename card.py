 
faces = ("TWO","THREE","FOUR",'FIVE','SIX','SEVEN','EIGHT',\
    'NINE','TEN','JACK','QUEEN','KING','ACE')
suits = ("CLUBS","DIAMONDS","HEARTS","SPADES")
   
class Card:

    #this constuctor can take two optional parameters
    #default card is ACE of SPADES
	def __init__(self, f="ACE",s="SPADES"):
		#set up a default card
		self.__face = ''
		self.__suit = ''
		#using the set methods to validate
		self.setFace(f)
		self.setSuit(s)
    
	def getSuit(self):
		#return the suit attribute
		return self.__suit
	
	def getFace(self):
		#return the face attribute
		return self.__face
	
	def setFace(self, val):
		val = str(val).upper()#convert to upper case string
		#store the faces in a tuple for later access
		#faces = ("TWO","THREE","FOUR",'FIVE','SIX','SEVEN','EIGHT',\
		#         'NINE','TEN','JACK','QUEEN','KING','ACE')
		if val.isdigit() and int(val) >= 2 and int(val) <= 10:
			self.__face = faces[int(val)-2]
		else:#value was not a valid number for a card, so check for others
			if val in faces:
				self.__face = val
			else:#not valid at all
				print("invalid face value:", val)
	
	def setSuit(self, s):
		s = str(s).upper()#convert to upper case string
		#store the suits in a tuple for later access
		#suits = ("CLUBS","DIAMONDS","HEARTS","SPADES")
		if s.isdigit() and int(s) >= 1 and int(s) <= 4:
			self.__suit = suits[int(s)-1]
		elif s in suits:#s was not a valid number, so check others
			self.__suit = s
		else:#not a valid suit at all
			print("invalid suit value:", s)
    
	def __str__(self):
    #method must return a string!
		return self.__face + ' of ' + self.__suit
