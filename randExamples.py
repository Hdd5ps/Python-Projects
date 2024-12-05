'''Random numbers
	Simulating craps games
	lab 9
	Oct. 24, 2024
'''

def rollDice():
	'''This function simulates rolling two 6-sided dice'''
	import random
	die1 = random.randrange(1,7)
	die2 = random.randrange(1,7)
	total = die1 + die2
	#print(die1,"+",die2,"=",total) #suppress printing
	return total


def playCraps():
	'''This function simulates one game of craps'''
	total = rollDice()
	#print("Come out roll: ", total) #suppress printing
	#did I win on the first roll?
	if total == 7 or total == 11:
		#print("You WON!")
		return "WIN"
	elif total == 2 or total == 3 or total == 12:
		#print("You LOST!")
		return "LOSE"
	else: 
		point = total
		#print("Your point is: ", point)
		#now do the point process
		#print("Reroll: ",end='')
		total = rollDice()
		#keep rolling until I get point or 7
		while total != point and total != 7:
			#keep rolling!
			#print("Reroll: ",end='')
			total = rollDice()
		#after
		#if got point, win
		if total == point:
			#print("You won the point.")
			return "WIN"
		else: #else got 7, so lose
			#print("You lost with a 7.")
			return "LOSE"
	


#main program 
def main():
	#this function handles the logic for simulating craps games
	
	#set up variable for wins
	wins = 0
	
	#varible for number of games to simulate
	games = 0
	#ask user for number of games to simulate
	while games <= 0: 
		games = int(input("How many games? (> 0) "))
		if games <= 0:
			print("That value is not positive. Try again.")
	
	#print a message
	print("Simulating", games, "games of craps...")
	
	#run the simulation
	for g in range(games):
		#play one game
		status = playCraps()
		if status == "WIN": #update wins if WIN
			wins += 1
	
	#print the summary
	winpercent = wins/games
	print("Won",wins,"of",games,"for a win percent of:",\
	      format(winpercent*100,'.2f'),end='')
	print("%")
	print("The house edge is:",\
	      format(1-winpercent-winpercent,'.4f'))
	
	
	
########################
#call the main function!
main() #this actually runs the main program












'''
#playing craps
answers = ["yes","YES","Yes","Y","y"]
answer = "yes"

while answer in answers:

	die1 = random.randrange(1,7)
	die2 = random.randrange(1,7)
	total = die1 + die2
	print(die1,"+",die2,"=",total)


	if total in [7,11]:
		print("WIN on come out roll!")
	elif total in [2,3,12]:
		print("LOSE on come out roll!")
	else: #point situation
		point = total
		print("Point set:", point)
		#reroll dice
		die1 = random.randrange(1,7)
		die2 = random.randrange(1,7)
		total = die1 + die2
		print(die1,"+",die2,"=",total)
		while total != point and total != 7:
			#keep rolling
			die1 = random.randrange(1,7)
			die2 = random.randrange(1,7)
			total = die1 + die2
			print(die1,"+",die2,"=",total)
			
		if total == point:
			print("WON by hitting point.")
		else:
			print("LOSE by hitting 7")
	answer = input("Play again? (yes or no):")
'''	
