if __name__ == '__main__':
    n = int(input())
    lists = map(int, input().split())
    print (hash(tuple(lists)))
