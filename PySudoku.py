# Sudoku is a puzzle on a 9x9 grid. Each box contains a number 1 thorugh 9. No number can be repeated in any single row or column.
# Additionally, there are nine 3x3 subgrids in which no number can be repeated
# This code searches for where numbers must be and stores them in their cells
import numpy as np

# xy is the 9x9 array which has numbers 1-9 to notate known numbers and 0 to notate unknown numbers
xy = np.zeros((9,9))

# zxy is another representation of xy. the third dimension corresponds to value.
# value of 1 indicates a known quantity. 0 indicates an unknown quantity. -1 indicates cell can't be a 1
# 1 in the [2][3][5] position would mean there's a 6 in the 3rd row and 6th column  
zxy = np.zeros((9,9,9))

unsolved = np.array(
 [[ 0., 0., 2., 7., 3., 0., 0., 6., 0.],
  [ 0., 3., 0., 0., 0., 0., 8., 0., 2.],
  [ 0., 0., 6., 0., 8., 0., 0., 9., 0.],
  [ 1., 0., 0., 0., 0., 0., 5., 0., 0.],
  [ 0., 0., 0., 3., 2., 6., 0., 0., 0.],
  [ 0., 0., 4., 0., 0., 0., 0., 0., 3.],
  [ 0., 4., 0., 0., 5., 0., 7., 0., 0.],
  [ 2., 0., 9., 0., 0., 0., 0., 1., 0.],
  [ 0., 6., 0., 0., 1., 7., 2., 0., 0.]])

solved =  np.array(
 [[ 8., 5., 2., 7., 3., 9., 4., 6., 1.],
  [ 9., 3., 7., 1., 6., 4., 8., 5., 2.],
  [ 4., 1., 6., 2., 8., 5., 3., 9., 7.],
  [ 1., 2., 3., 4., 9., 8., 5., 7., 6.],
  [ 7., 9., 5., 3., 2., 6., 1., 4., 8.],
  [ 6., 8., 4., 5., 7., 1., 9., 2., 3.],
  [ 3., 4., 1., 6., 5., 2., 7., 8., 9.],
  [ 2., 7., 9., 8., 4., 3., 6., 1., 5.],
  [ 5., 6., 8., 9., 1., 7., 2., 3., 4.]])



def store_number(x,y,z): #x = which row, y = which column, z = what number
	
	xy[x][y] = z #stores number in x,y
	for i in range(9): #places -1 in locatinos numbers can't be.
		zxy[i][x][y] = -1
		zxy[z-1][i][y] = -1
		zxy[z-1][x][i] = -1
	subgrid_rule_out(x,y,z)
	zxy[z-1][x][y] = z   #for debugging to see what slice I'm in more easily
	#zxy[z-1][x][y] = 1   #when not debugging.
	#print(x,y,z, zxy[x][y][z-1])
	#print("I stored a %d in row %d, column %d" % (z,x,y))

#function used in store_number()
def subgrid_rule_out(x,y,z):
	# identifies which 3x3 subgrid store_number is storing
	xbox = (x)//3
	ybox = (y)//3
	
	for i in range(3):
		for j in range(3):
			zxy[z-1][i+(xbox*3)][j+(ybox*3)] = -1
			zxy[z-1][i+(xbox*3)][j+(ybox*3)] = -1


#searching rows for all -1 except a 0. When found will store_number()
def search_rows():
	tempy = zxy.sum(axis = 2)
	#print (zxy)
	#print(tempy)
	counter = 0
	for a in np.argwhere(tempy == -8):
		#print(a[0],a[1])
		for i in range(9):
			#print(zxy[a[0]][a[1]][i], i,a)
			if zxy[a[0]][a[1]][i] == 0:
				#print("i =",i, "a[0] =", a[0], "a[1] =",a[1])
				store_number(a[1],i,(a[0]+1))
				#counter += 1
	#print (counter)


def search_cols():
	tempx = zxy.sum(axis = 1)
	#counter = 0
	#print(zxy)
	#print(tempx)
	for a in np.argwhere(tempx == -8):
		#print(a[0], "THIS + 1 IS THE NUMBER(Z)")
		for i in range(9):
			#print("zxy[a[0]][i][a[1]] contains ", zxy[a[0]][i][a[1]], ", i =",i, ", a[0] =", a[0], ", a[1] =",a[1])
			if zxy[a[0]][i][a[1]] == 0:
				store_number(i,a[1],(a[0]+1))
				#counter += 1



def check_finished(board):
	one_to_nine = (np.arange(1.,10.)) #creates 1d array with values 1-9
	finished_subgrid = np.arange(1.,10.).reshape(3,3) #reshapes to 3x3 array
	one_to_nines = ((np.arange(1., 82)%9)+1) #creates 1d array with values 1-9 nine times
	finished_grid = np.sort(np.reshape(one_to_nines,(9,9))) #reshapes then sorts into 9x9 array
	#print(finished_subgrid)
	#print(finished_grid)
	if (np.count_nonzero(solved.sum(axis = 0)-45) == 0) and np.count_nonzero(solved.sum(axis = 1)-45) == 0:
		if (np.array_equal(finished_grid, np.sort(solved))):
			print("ALL DONE!!!!")
	else:
		print("not done yet...")



#def search_subgrid():


#####################################################################################
#####################################################################################

#populates matrix with input sudoku
for i in range(9):
	for j in range(9):
		if unsolved[i][j] != 0:
			store_number(i,j,unsolved[i][j])

#####################################################################################
#####################################################################################

"""def search_depth():
	tempz = zxy.sum(axis = 0)
	print(tempz)
"""


for t in range(99):
	search_cols()
	search_rows()
print (unsolved)
print (xy)


"""for i in range(9):
	for j in range(9):
		if np.count_nonzero(zxy[i][j]) == 8:
			print(i,j)
"""



a = (zxy.sum(axis = 1)) #
#print (zxy[0::9].sum(axis = 2))
"""def search_depth():
	for n in range(9):
		for m in range(9):
			print(n,m, zxy[n][m].sum(axis = 0))
"""
#print (zxy)
#print (xy)
#print (unsolved)
#search_depth()


#print(np.sort(solved))



"""
unsolved1 =
 [[ 0.  0.  2.  7.  3.  0.  0.  6.  0.]
  [ 0.  3.  0.  0.  0.  0.  8.  0.  2.]
  [ 0.  0.  6.  0.  8.  0.  0.  9.  0.]
  [ 1.  0.  0.  0.  0.  0.  5.  0.  0.]
  [ 0.  0.  0.  3.  2.  6.  0.  0.  0.]
  [ 0.  0.  4.  0.  0.  0.  0.  0.  3.]
  [ 0.  4.  0.  0.  5.  0.  7.  0.  0.]
  [ 2.  0.  9.  0.  0.  0.  0.  1.  0.]
  [ 0.  6.  0.  0.  1.  7.  2.  0.  0.]]

solved1 = 
 [[ 8.  5.  2.  7.  3.  9.  4.  6.  1.]
  [ 9.  3.  7.  1.  6.  4.  8.  5.  2.]
  [ 4.  1.  6.  2.  8.  5.  3.  9.  7.]
  [ 1.  2.  3.  4.  9.  8.  5.  7.  6.]
  [ 7.  9.  5.  3.  2.  6.  1.  4.  8.]
  [ 6.  8.  4.  5.  7.  1.  9.  2.  3.]
  [ 3.  4.  1.  6.  5.  2.  7.  8.  9.]
  [ 2.  7.  9.  8.  4.  3.  6.  1.  5.]
  [ 5.  6.  8.  9.  1.  7.  2.  3.  4.]]
"""
