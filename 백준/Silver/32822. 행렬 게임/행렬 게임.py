import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst1 = [list(map(int,input().split())) for _ in range(n)]
lst2 = [list(map(int,input().split())) for _ in range(n)]

p = [0]*n
for j in range(n):
    for i in range(n):
        p[j] = max(p[j], abs(lst1[i][j] - lst2[i][j]))

query = list(map(int,input().split()))
res = 0
for i in query:
    res += p[i-1]

print(res)