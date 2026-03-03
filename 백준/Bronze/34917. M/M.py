t = int(input())
for case in range(t):
    n = int(input())
    lst = [['.']*n for _ in range(n)]
    for i in range(n):
        lst[i][0] = '#'
        lst[i][n-1] = '#'

    for i in range(n//2 + 1):
        lst[i][i] = '#'
        lst[i][n-1-i] = '#'

    for i in lst:
        print(*i,sep='')