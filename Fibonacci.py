def Fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (Fibonnaci(n-1)+ Fibonnaci(n-2))

n = int(input())
print(Fibonnaci(n))
start,end = [int(s) for s in input().split()]
print (list(map(Fibonnaci,range(start,end))))
#7
#13
#1 5
#[1, 1, 2, 3]
#################################################
def fib(n):
     count = 0
     a, b = 0, 1
     while count < n:
             yield a
             a, b = b, a + b
             count += 1
[i for i in fib(10)]

####################################################


