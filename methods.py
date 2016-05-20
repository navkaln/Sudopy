import numpy as np

def store_number(coords, board): #x = which row, y = which column, z = what number
	print(coords)
	z = coords[0]
	x = coords[1]
	y = coords[2]
	#xy[x][y] = z #stores number (z) in x,y
	for i in range(9): #places -1 in locatinos numbers can't be.
		board[i][x][y] = -1
		board[z-1][i][y] = -1
		board[z-1][x][i] = -1
	subgrid_rule_out(coords, board)
	board[z-1][x][y] = z   #for debugging to see what slice I'm in more easily
	#board[z-1][x][y] = 1   #when not debugging.
	#print(x,y,z, board[x][y][z-1])
	print("I stored a %d in row %d, column %d" % (z,x,y))

#function used in store_number()
def subgrid_rule_out(coords, board):
	# identifies which 3x3 subgrid store_number is storing
	zz = coords[0]
	xx = coords[1]
	yy = coords[2]
	xbox = (xx)//3
	ybox = (yy)//3
	for i in range(3):
		for j in range(3):
			board[zz-1][i+(xbox*3)][j+(ybox*3)] = -1
			board[zz-1][i+(xbox*3)][j+(ybox*3)] = -1


#searching rows for all -1 except a 0. 
def search_rows(board):
	tempy = board.sum(axis = 2)
	#print (board)
	#print(tempy)
	#counter = 0
	for a in np.argwhere(tempy == -8):
		print(a[0],a[1], "I found a ", a[0]+1, "to be placed somewhere in row", a[1]+1, ". Let's go search where it goes")
		for i in range(9):
			#print(board[a[0]][a[1]][i], i,a)
			if board[a[0]][a[1]][i] == 0:
				print("i =",i, "a[0] =", a[0], "a[1] =",a[1])
				#store_number(a[1],i,(a[0]+1))
				return ((a[0]+1), a[1], i)
				#counter += 1
	#print (counter)


def search_cols(board):
	tempx = board.sum(axis = 1)
	#counter = 0
	#print(board)
	#print(tempx)
	for a in np.argwhere(tempx == -8):
		print(a[0],a[1], "I found a ", a[0]+1, "to be placed somewhere in column", a[1]+1, ". Let's go search where it goes")
		for i in range(9):
			#print("board[a[0]][i][a[1]] contains ", board[a[0]][i][a[1]], ", i =",i, ", a[0] =", a[0], ", a[1] =",a[1])
			if board[a[0]][i][a[1]] == 0:
				return((a[0]+1), i, a[1])
				#store_number(i,a[1],(a[0]+1))
				#counter += 1

def search_depths(board):
	tempz = board.sum(axis = 0)
	#counter = 0
	#print(board)
	#print(tempz)
	for a in np.argwhere(tempz == -8):
		print("I found a number must be in coordinates:", a[0], a[1], ". Let's find out what number it is.")
		for i in range(9):
			#print("board[a[0]][i][a[1]] contains ", board[a[0]][i][a[1]], ", i =",i, ", a[0] =", a[0], ", a[1] =",a[1])
			if board[i][a[0]][a[1]] == 0:
				return((i+1), a[0], a[1])
				#store_number(i,a[1],(a[0]+1))
				#counter += 1

def get_threebythree(board): #looks at 3x3 boxes to find instances of eight -1's and one 0, signifying the zero must be turned into a 1
    for i in range(9):#search every slice in depth (z-axis)
        number = i+1
        #print(number, "number")
        for ybox in range(3):#searches every column of boxes
            #print(ybox, "ybox")
            for xbox in range(3):#and every row of boxes
                #print(xbox, "xbox")
                if(np.count_nonzero(board[i,(ybox*3):(ybox*3+3),(xbox*3):(xbox*3+3)]) == 8): #if box has eight -1s
                    print("FOUND!!!", i, ybox, xbox) #FOUND!!!
                    for m in range(3):
                        for n in range(3): #finds coordinates of 0 in box
                            if board[i, (ybox*3)+ m, (xbox*3)+ n] == 0:
                                return (i+1, (ybox*3)+ m, (xbox*3)+ n) #returns coords where known number was found! (number, y coordinate, xcoordinate)


def threetotwodimensions(board, boardina):
	for a in range(9):
		for b in range(9):
			for c in range(9):
				if board[a,b,c] > 0:
					#print(board[a,b,c])
					boardina[b,c] = a+1
