import numpy as np
import methods

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



for i in range(9):
    for j in range(9):
        if unsolved[i][j] != 0:
            methods.store_number((unsolved[i][j],i,j), zxy)
#print(zxy)
for qqq in range(20):
    tostore = methods.get_threebythree(zxy)
    if tostore != None:#if you found something
        methods.store_number(tostore, zxy)# store it
    tostore = methods.search_rows(zxy)#try rows
    if tostore != None:
        methods.store_number(tostore, zxy)
    tostore = methods.search_cols(zxy)
    if tostore != None:
        methods.store_number(tostore, zxy)
    tostore = methods.search_depths(zxy)
    if tostore != None:
        methods.store_number(tostore, zxy)
    print(qqq)

methods.threetotwodimensions(zxy,xy)
print(xy)
