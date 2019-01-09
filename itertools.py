from itertools import combinations

_,s,n = input(),input().split(),int(input())
t = list(combinations(s,n))
f = [i for i in t if 'a' in i]
print("{0:.12}".format(len(f)/len(t))) 


from itertools import combinations

N = int(input())
L = input().split()
K = int(input())
C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))


'''The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.'''

'''Sample Input

4 
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length  comprising of indices from  to  are:


Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.

Hence, the answer is .'''

