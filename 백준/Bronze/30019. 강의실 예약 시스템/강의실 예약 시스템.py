import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [0]*(n+1)
for i in range(m):
    k,s,e = map(int,input().split())
    if lst[k] <= s:
        lst[k] = e
        print('YES')
    else:
        print('NO')