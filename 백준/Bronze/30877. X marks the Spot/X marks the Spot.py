import sys
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    s,t = input().split()
    for i in range(len(s)):
        if s[i] in ('x','X'):
            res.append(t[i].upper())

print(''.join(res))