from itertools import product
K,M = map(int,input().split())
#print (K,M)
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

(5^2 + 9^2 + 10^2)/ 1000 = 206
 

 '''"The next lines each contains an integer Ni followed by Ni space separated integers denoting the elements in the list."

So the first number is the number of numbers. We don't need that.

For example: 5 5 7 8 9 10

5 is how many numbers there are in the list (5,7,8,9,10)

product(*N) is itertools.product(*N) which is the same as itertools.product(N[0],N[1],...,N[K-1])

It's the cartesian product of all the tuples in in N.
'''
