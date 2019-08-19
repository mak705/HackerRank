def alphaBeta(pile):
    pileMax = max(pile)
    newPile = [i for i in pile if i != pileMax]
    print (newPile)
    if len(newPile) > 0:
        return max(newPile)
    return 0
if __name__ == '__main__':
    n = int(input().strip())
    pile = list(map(int, input().rstrip().split()))
    result = alphaBeta(pile)
    print (result)

#5
#1 2 2 3 3
#[1, 2, 2]
############################
def high(arr = []):
    for i in range(len(arr)):
        arr = list(set(arr))
        #print (arr)
        arr[arr.index(max(arr))] = 0
        return max(arr)
high([1,2,3,4,5,5])
