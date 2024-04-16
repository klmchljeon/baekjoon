import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
d = [[] for _ in range(4)]
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in range(4):
        d[i].append(tmp[i])

dic1 = defaultdict(int)
for i in range(n):
    for j in range(n):
        dic1[d[0][i]+d[1][j]] += 1

cnt = 0
for i in range(n):
    for j in range(n):
        t = -(d[2][i]+d[3][j])
        if t in dic1:
            cnt += dic1[t]

print(cnt)