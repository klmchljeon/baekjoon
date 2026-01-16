import sys
input = sys.stdin.readline

n,m = map(int,input().split())
for _ in range(m):
    u,v = map(int,input().split())

if n >= m:
    print('Yes')
else:
    print('No')