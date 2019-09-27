arr = [5,4,3,1,6,8,10,9] # array not sorted

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

            print (arr)
            
#[4, 5, 3, 1, 6, 8, 10, 9]
#[3, 5, 4, 1, 6, 8, 10, 9]
#[1, 5, 4, 3, 6, 8, 10, 9]
#[1, 4, 5, 3, 6, 8, 10, 9]
#[1, 3, 5, 4, 6, 8, 10, 9]
#[1, 3, 4, 5, 6, 8, 10, 9]
#[1, 3, 4, 5, 6, 8, 9, 10]

