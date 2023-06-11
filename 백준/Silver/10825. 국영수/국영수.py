#국영수
import sys
input = sys.stdin.readline

f = lambda x:(-x[1],x[2],-x[3],x[0])

n = int(input())
d = []
for _ in range(n):
    name,*score = input().split()
    a,b,c = map(int,score)
    d.append((name,a,b,c))

d.sort(key = f)

for i in d:
    print(i[0])