import sys
from heapq import *
input = sys.stdin.readline

h = int(input())
n,q = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

heap = []
s = 0
while lst and s<h:
    tmp = lst.pop()
    s += tmp
    heappush(heap,tmp)

print(len(heap) if s>=h else -1)
for _ in range(q):
    x = int(input())

    flag = False
    if s>=h:
        while heap and heap[0]<=x and s-heap[0]+x>=h:
            s -= heappop(heap)
            flag = True

    else:
        flag = True

    if flag:
        heappush(heap,x)
        s += x

    

    print(len(heap) if s>=h else -1)
