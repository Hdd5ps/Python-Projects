'''
	Tic Tac Toe
'''
def convert(val):
	values = [ "0 0", "0 1", "0 2", "1 0", "1 1", "1 2", "2 0", "2 1", "2 2"]
	return values[val - 1].split()

def printBoard(b):
	print(b[0][0],"|",b[0][1],"|",b[0][2])
	print("----------")
	print(b[1][0],"|",b[1][1],"|",b[1][2])
	print("----------")
	print(b[2][0],"|",b[2][1],"|",b[2][2])

def checkWin(b, c):
	stat = "ongoing"
	if b[0][0] == 'X' and b[0][1] == 'X' and b[0][2] == 'X'\
	or b[1][0] == 'X' and b[1][1] == 'X' and b[1][2] == 'X'\
	or b[2][0] == 'X' and b[2][1] == 'X' and b[2][2] == 'X'\
	or b[0][0] == 'X' and b[1][0] == 'X' and b[2][0] == 'X'\
	or b[0][1] == 'X' and b[1][1] == 'X' and b[2][1] == 'X'\
	or b[0][2] == 'X' and b[1][2] == 'X' and b[2][2] == 'X'\
	or b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X'\
	or b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X':
		stat = "X wins"
	if b[0][0] == 'O' and b[0][1] == 'O' and b[0][2] == 'O'\
	or b[1][0] == 'O' and b[1][1] == 'O' and b[1][2] == 'O'\
	or b[2][0] == 'O' and b[2][1] == 'O' and b[2][2] == 'O'\
	or b[0][0] == 'O' and b[1][0] == 'O' and b[2][0] == 'O'\
	or b[0][1] == 'O' and b[1][1] == 'O' and b[2][1] == 'O'\
	or b[0][2] == 'O' and b[1][2] == 'O' and b[2][2] == 'O'\
	or b[0][0] == 'O' and b[1][1] == 'O' and b[2][2] == 'O'\
	or b[0][2] == 'O' and b[1][1] == 'O' and b[2][0] == 'O':
		stat = "O wins"
	if c == 9 and stat == "ongoing":
		stat = "tie"

	return stat

def playTicTacToe(b):
	#ask user for play spot
	status = "ongoing"
	chars = ['O','X']
	player = 1
	counter = 0
	while status == "ongoing":
		val = int(input("Player "+str(player)+" move: "))
		if val < 1 or val > 9:
			print("Not a valid value. Try again.")
			continue
		x,y = convert(val)
		x = int(x)
		y = int(y)
		if b[x][y] == 'X' or b[x][y] == 'O':
			print("Spot already taken. Try again.")
			continue
		b[x][y] = chars[player]
		counter += 1
		#update player
		player = (player + 1) % 2
		printBoard(b)
		#check for a win
		status = checkWin(b, counter)
	print(status)
	
def main():

	board = [ [1,2,3],
	          [4,5,6],
	          [7,8,9] ]
	printBoard(board)
	playTicTacToe(board)
	
	
main()
