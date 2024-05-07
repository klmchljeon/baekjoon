import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]
d.sort()

res = int(1e9)
for i in range(n//2):
    res = min(res,d[i]+d[n-i-1])\

print(res)