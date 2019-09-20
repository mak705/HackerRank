#Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the #strings share a common substring.

#twoStrings has the following parameter(s):

#s1, s2: two strings to analyze .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    return 'YES' if any(i in s2 for i in s1 ) else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
