def high(arr,n):
    for i in range(n+ 1 ):
        arr[arr.index(max(arr))] = 0
        return max(arr)
high([1,2,3,4,5], 2)


