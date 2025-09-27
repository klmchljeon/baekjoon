import sys
from collections import deque
input = sys.stdin.readline
 
n,p,k = map(int,input().split())
lst = []
for _ in range(n):
    t,a = map(int,input().split())
    lst.append((t,a))
 
lst.sort()
 
queue = [deque([]) for _ in range(k+1)]
for t,a in lst:
    queue[a].append(t)
 
cnt = n
cur = ((lst[0][0]-1)//p + 1)*p
idx = 0
res = 0
while cnt:
    t = int(1e9)
    for i in range(1,k+1):
        if queue[i] and t > queue[i][0]:
            t = queue[i][0]
 
    tmp = ((t-1)//p + 1)*p
    cur = max(cur,tmp)
 
    m = k
    while m:
        t = cur+1
        x = -1
        for i in range(1,m+1):
            if queue[i] and t > queue[i][0]:
                t = queue[i][0]
                x = i
 
        if x == -1:
            break
 
        res += cur - t
        m -= x
        queue[x].popleft()
        cnt -= 1
 
    cur += p
 
print(res)
