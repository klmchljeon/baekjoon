#다각형의 면적
import sys
input = sys.stdin.readline

n = int(input())
d = []
for _ in range(n):
    x,y = map(int,input().split())
    d.append((x,y))

d.append(d[0])

res = [0,0]
for i in range(n):
    for j in (0,1):
        res[j] += d[i][j]*d[i+1][j^1]

print(round(abs(res[0]-res[1])/2,2))