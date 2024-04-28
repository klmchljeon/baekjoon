import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
d = []
for _ in range(n):
    p,q = map(int,input().split())
    d.append((p,q))

d.sort()

cnt = []
heap1 = list(range(n))
heapify(heap1)

heap2 = []
for s,e in d:
    while heap2:
        t,num = heap2[0]
        if t <= s:
            heappush(heap1,num)
            heappop(heap2)

        else:
            break
    
    k = heappop(heap1)
    if k >= len(cnt):
        cnt.append(0)

    cnt[k] += 1

    heappush(heap2,(e,k))

print(len(cnt))
print(*cnt)