from heapq import *

n,m,k = map(int,input().split())
res = 0
cur = 0

heap = []
for _ in range(n):
    d = int(input())
    heappush(heap,-d)

res = []
while heap:
    p = -heappop(heap)
    cur = cur//2 + p
    res.append(cur)

    p -= m
    if p > k:
        heappush(heap,-p)

print(len(res))
print(*res,sep = '\n')