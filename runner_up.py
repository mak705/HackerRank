if __name__ == '__main__':
    dn,arr=(input() for _ in range(2))
    nums = map(int, arr.split())
    a=sorted(list(set(nums)))
    if(len(a)==1):
        print(a[0])
    else:
        print(a[-2])


Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
