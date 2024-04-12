import sys
input = sys.stdin.readline
max_ = 1000000

n,k = map(int,input().split())
lst = []
for i in range(n):
    g,x = map(int,input().split())
    lst.append((x,g))

lst.sort()

res = 0
dis = 0
tmp = 0
e = 0
for s in range(n):
    while e<n and lst[e][0]-lst[s][0]<=2*k:
        tmp += lst[e][1]
        e += 1

    res = max(res,tmp)
    tmp -= lst[s][1]

print(res)