"""
'Python-is-Easy' Project #1 (Connect 4)
DESCRIPTION: 
This is the first project in the 'Python is Easy' course from Pirple..

The assignment is to create the popular two player game called Connect 4, using Python code.


Will start by first manually drawing out the board.

| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
| | | | | | | |
---------------
|1|2|3|4|5|6|7|
---------------

|_|_|_|_|_|_|_| 
|_|_|_|_|_|_|_| 
|_|_|_|_|_|_|_| 
|_|_|_|_|_|_|_| 
|_|_|_|_|_|_|_| 
|_|_|_|_|_|_|_| 
 1 2 3 4 5 6 7 

0...	
.0..
..0.
...0

0	.	.	.
 .	 0	 .	 .
  .	  .	  0	  .
   .   .   .   0
"""

def drawGamepPlay(move):
	for row in range(7): 
		for col in range(16):
			columnNumber = int((col+1)/2)
			if col == 15:
				print(" ")
				break
			if row == 6:
				if col%2 ==0:
					print(" ",end="")
				else:
					print(columnNumber,end="")
				continue
			if col%2 == 0:
				print("|",end="")
			else:
				print(move[columnNumber-1][row],end="")

GameStatus = [["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"]]

Player = 1
drawGamepPlay(GameStatus)

def checkline1_1():
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot] == GameStatus[int(playermove)+1][colslot] == GameStatus[int(playermove)+2][colslot]:
		#print("1.1")
		winner()
def checkline1_2():
	if GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot] == GameStatus[int(playermove)+1][colslot]:
		#print("1.2")
		winner()
def checkline1_3():
	if GameStatus[int(playermove)-3][colslot] == GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot]:
		#print("1.3")
		winner()
def checkline1_4():
	if GameStatus[int(playermove)-4][colslot] == GameStatus[int(playermove)-3][colslot] == GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot]:
		#print("1.4")
		winner()
def checkline2_1():
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)-1][colslot+1] == GameStatus[int(playermove)-1][colslot+2] == GameStatus[int(playermove)-1][colslot+3]:
		#print("2.1")
		winner()
def checkline3_1():
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1] == GameStatus[int(playermove)+1][colslot-2] == GameStatus[int(playermove)+2][colslot-3]:
		#print("3.1")
		winner()
def checkline3_2():
	if GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1] == GameStatus[int(playermove)+1][colslot-2]:
		#print("3.2")
		winner()
def checkline3_3():
	if GameStatus[int(playermove)-3][colslot+2] == GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1]:
		#print("3.3")
		winner()
def checkline3_4():
	if GameStatus[int(playermove)-4][colslot+3] == GameStatus[int(playermove)-3][colslot+2] == GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot]:
		#print("3.4")
		winner()
def checkline4_1():
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1] == GameStatus[int(playermove)+1][colslot+2] == GameStatus[int(playermove)+2][colslot+3]:
		#print("4.1")
		winner()
def checkline4_2():
	if GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1] == GameStatus[int(playermove)+1][colslot+2]:
		#print("4.2")
		winner()
def checkline4_3():
	if GameStatus[int(playermove)-3][colslot-2] == GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1]:
		#print("4.3")
		winner()
def checkline4_4():
	if GameStatus[int(playermove)-4][colslot-3] == GameStatus[int(playermove)-3][colslot-2] == GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot]:
		#print("4.4")
		winner()

def winner():
	drawGamepPlay(GameStatus)
	print("\n\nGAME OVER! \n\nPlayer",Player,"WINS!")
	exit()

def checkwin():
	for y in range(7):
		for x in range(5,-1,-1):
			if int(playermove)-1 == y and colslot == x:
				if y == 0 and x > 2:
					checkline1_1()
					checkline3_1()
					#print("WINNER118")
				if y == 1 and x > 2:
					checkline1_1()
					checkline1_2()
					checkline3_1()
					#print("WINNER123")
					if x < 5:
						checkline3_2()
					#	print("WINNER126")
						if x < 4:
							checkline4_2()
					#		print("WINNER129")
				if y == 2 and x > 2:
					checkline1_1()
					checkline1_2()
					checkline1_3()
					checkline3_1()
					#print("WINNER135")
					if x < 5:
						checkline3_2()
					#	print("WINNER138")
						if x < 4:
							checkline3_3()
					#		print("WINNER141")					
				if y == 3 and x > 2:
					checkline1_1()
					checkline1_2()
					checkline1_3()
					checkline1_4()
					checkline3_1()
					checkline4_4()
					#print("WINNER149")
					if x < 5:
						checkline3_2()
						checkline4_3()
					#	print("WINNER153")
						if x < 4:
							checkline3_3()
							checkline4_2()
					#		print("WINNER157")
				if y == 4 and x > 2:
					checkline1_2()
					checkline1_3()
					checkline1_4()
					checkline4_4()
					#print("WINNER163")
					if x < 5:
						checkline4_3()
					#	print("WINNER166")
						if x < 4:
							checkline4_2()
					#		print("WINNER169")
				if y == 5 and x > 2:
					checkline1_3()
					checkline1_4()
					checkline4_4()
					#print("WINNER174")
					if x < 5:
						checkline4_3()
					#	print("WINNER177")
				if y == 6 and x > 2:
					checkline1_4()
					checkline4_4()
					#print("WINNER181")
				if y == 3 and x < 3:
					checkline1_1()
					checkline1_2()
					checkline1_3()
					checkline1_4()
					checkline2_1()
					checkline3_4()
					checkline4_1()
					#print("WINNER190")
					if x > 0:
						checkline3_3()
						checkline4_2()
					#	print("WINNER194")
						if x > 1:
							checkline3_2()
							checkline4_3()
					#		print("WINNER198")							
				if y == 2 and x < 3:
					checkline1_1()
					checkline1_2()
					checkline1_3()
					checkline2_1()
					checkline4_1()
					#print("WINNER205")
					if x > 0:
						checkline3_3()
						checkline4_2()
					#	print("WINNER209")
						if x > 1:
							checkline3_2()
							checkline4_3()
					#		print("WINNER213")
				if y == 1 and x < 3:
					checkline1_1()
					checkline1_2()
					checkline2_1()
					checkline4_1()
					#print("WINNER219")
					if x > 0:
						checkline4_2()
					#	print("WINNER222")
						if x > 1:
							checkline3_2()
					#		print("WINNER225")		
				if y == 0 and x < 3:
					checkline1_1()
					checkline2_1()
					checkline4_1()
					#print("WINNER230")					
				if y == 4 and x < 3:
					checkline1_2()
					checkline1_3()
					checkline1_4()
					checkline2_1()
					checkline3_4()
					#print("WINNER237")
					if x > 0:
						checkline3_3()
						checkline4_2()
					#	print("WINNER241")
						if x > 1:
							checkline4_3()
							checkline3_2()
					#		print("WINNER245")
				if y == 5 and x < 3:
					checkline1_3()
					checkline1_4()
					checkline2_1()
					checkline3_4()
					#print("WINNER251")
					if x > 0:
						checkline3_3()
					#	print("WINNER254")
						if x > 1:
							checkline4_3()
					#		print("WINNER257")
				if y == 6 and x < 3:
					checkline1_4()
					checkline2_1()
					checkline3_4()
					#print("WINNER263")

while(True):
	print("=========================\n\nPlayers Turn:", "Player",Player)
	playermove = input("Select column: ")
	if GameStatus[int(playermove)-1][0] != "_":
		print("=========================\n\nCareful! Column",playermove,"is full.\nChoose a column with at least one empty space!")
		continue
	colslot = -1
	if Player == 1:
		for n in GameStatus[int(playermove)-1]:
			if n == "_":
				colslot += 1
				if colslot == 5:
					GameStatus[int(playermove)-1][colslot] = "X"
					checkwin()
					Player = 2
					break
			else:
				GameStatus[int(playermove)-1][colslot] = "X"
				checkwin()
				Player = 2
				break
	else:
		for n in GameStatus[int(playermove)-1]:
			if n == "_":
				colslot += 1
				if colslot == 5:
					GameStatus[int(playermove)-1][colslot] = "O"
					checkwin()
					Player = 1
					break
			else:
				GameStatus[int(playermove)-1][colslot] = "O"
				checkwin()
				Player = 1
				break
	drawGamepPlay(GameStatus)


############# draft work below ###############
# while(True):
# 	print("\n\nPlayers Turn:", "Player",Player)
# 	playermove = input("Select column:\n")
# 	if GameStatus[int(playermove)-1][0] != "_":
# 		print("\n\nCareful! Column",playermove,"is full.\nChoose a column with at least one empty space!")
# 		continue
# 	colslot = -1
# 	if Player == 1:
# 		if GameStatus[int(playermove)-1][5] == "_":
# 			GameStatus[int(playermove)-1][5] = "X"
# 			checkwin()
# 			Player = 2
# 		else:
# 			for n in GameStatus[int(playermove)-1]:
# 				if n == "_":
# 					colslot += 1
# 				else:
# 					GameStatus[int(playermove)-1][colslot] = "X"
# 					checkwin()
# 					Player = 2
# 					break
# 	else:
# 		if GameStatus[int(playermove)-1][5] == "_":
# 			GameStatus[int(playermove)-1][5] = "O"
# 			checkwin()
# 			Player = 1
# 		else:
# 			for n in GameStatus[int(playermove)-1]:
# 				if n == "_":
# 					colslot += 1
# 				else:
# 					GameStatus[int(playermove)-1][colslot] = "O"
# 					checkwin()
# 					Player = 1
# 					break
# 	drawGamepPlay(GameStatus)


############## below is the draft code for checking the win, all possible line combos #####################

				# if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot] == GameStatus[int(playermove)+1][colslot] == GameStatus[int(playermove)+2][colslot]:
				# 	print("1.1")
				# if GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot] == GameStatus[int(playermove)+1][colslot]:
				# 	print("1.2")
				# if GameStatus[int(playermove)-3][colslot] == GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot]:
				# 	print("1.3")
				# if GameStatus[int(playermove)-4][colslot] == GameStatus[int(playermove)-3][colslot] == GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot]:
				# 	print("1.4")
				# if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)-1][colslot+1] == GameStatus[int(playermove)-1][colslot+2] == GameStatus[int(playermove)-1][colslot+3]:
				# 	print("2.1")
				# if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1] == GameStatus[int(playermove)+1][colslot-2] == GameStatus[int(playermove)+2][colslot-3]:
				# 	print("3.1")
				# if GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1] == GameStatus[int(playermove)+1][colslot-2]:
				# 	print("3.2")
				# if GameStatus[int(playermove)-3][colslot+2] == GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1]:
				# 	print("3.3")
				# if GameStatus[int(playermove)-4][colslot+3] == GameStatus[int(playermove)-3][colslot+2] == GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot]:
				# 	print("3.4")
				# if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1] == GameStatus[int(playermove)+1][colslot+2] == GameStatus[int(playermove)+2][colslot+3]:
				# 	print("4.1")
				# if GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1] == GameStatus[int(playermove)+1][colslot+2]:
				# 	print("4.2")
				# if GameStatus[int(playermove)-3][colslot-2] == GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1]:
				# 	print("4.3")
				# if GameStatus[int(playermove)-4][colslot-3] == GameStatus[int(playermove)-3][colslot-2] == GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot]:
				# 	print("4.4")
