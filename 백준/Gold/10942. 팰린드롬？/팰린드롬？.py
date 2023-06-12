#팰린드롬? 08:26
import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))

lst = [[0]*n for _ in range(n)]
for i in range(n):
    l,r = i,i
    while 0<=l and r<n:
        if d[l]==d[r]:
            lst[l][r] = 1
        else:
            break

        l -= 1
        r += 1

    l,r = i,i+1
    while 0<=l and r<n:
        if d[l]==d[r]:
            lst[l][r] = 1
        else:
            break

        l -= 1
        r += 1

m = int(input())
for query in range(m):
    s,e = map(int,input().split())
    print(lst[s-1][e-1])