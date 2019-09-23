#Transpose

import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]
 
 #Flatten
 import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]

import numpy as np
n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())

Input (stdin)
2 2
1 2
3 4

Out
[[1 3]
 [2 4]]
[1 2 3 4]
#################################################################
import numpy as np
N, M = list(map(int, input().split()))
a = np.array([input().split() for _ in range(N)], int)
print(a.T, a.flatten(), sep='\n')
print (a)

Input
2 3
1 2 3
4 5 6

Out
[[1 4]
 [2 5]
 [3 6]]
[1 2 3 4 5 6]
#a
array([[1, 2, 3],
       [4, 5, 6]])
       
####################################################
