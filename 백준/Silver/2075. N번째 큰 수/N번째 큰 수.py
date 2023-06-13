#N번째 큰 수
import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    d = map(int,input().split())
    
    for i in d:
        heappush(heap,i)

    while len(heap) > n:
        heappop(heap)

res = heappop(heap)
print(res)