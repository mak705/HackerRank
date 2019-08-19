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
