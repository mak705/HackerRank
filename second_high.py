if __name__ == '__main__':
    markesheet = []
    n = int(input())
    markesheet = [[input(), float(input())] for _ in range(n)]
    second_last_mark = sorted(list(set([marks for name,marks in markesheet])))[1]
    print ('\n'.join([a for a,b in sorted(markesheet) if b ==  second_last_mark]))

