n = int(input().strip())
p = list(map(int,input().strip().split(' ')))
for i in range(n):   
    print(p.index(p.index(i+1)+1)+1)

''' Our task is :: For each x from 1 to n , print an integer denoting any valid y satisfying the equation p(p(y)) = x on a new line.
Here p(y) means, the value at y index in list p. But the range of y goes from 1 to n, and range of python list goes from 0 to n-1. so make it balanced, we need to add 1 in each time in y to make it equal to python index.

for example
3
2 3 1

Now, x goes from 1 to 3 (inclusive), but since the range goes from 0 to n-1, 1 needed to add here to balance it.

when i = 0, x = i+1, you need to find that at which index 1 is coming in list p
first_index = p.index(i+1)
now, u need to find at which index the first_index is coming, but since , the index coming as output in above line is from 0 to  n-1, 1 needed to add to balace it

second_index = p.index(first_index+1)

since this will also be 0 to n-1,, add 1

ans = second_index + 1

I have written a new code so u can understand how each line works
'''

n = int(input().strip())
p = list(map(int,input().strip().split(' ')))
for i in range(n):    
    x = i+1
    first_index = p.index(x)
    second_index = p.index(first_index + 1)
    ans = second_index + 1
    print(ans)
    
    
    
 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    return [(p.index(p.index(i)+1)+1) for i in range(1, max(p)+1)]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
Input (stdin)
3
2 3 1
Expected Output
2
3
1
