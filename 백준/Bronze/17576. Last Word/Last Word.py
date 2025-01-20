import sys
input = sys.stdin.readline

st = input().rstrip()
n = int(input())
s,l = 0,0
for _ in range(n):
    a,b = map(int,input().split())
    s += a
    l = b

print(st[s:s+l])