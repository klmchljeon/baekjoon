#실행 시간
import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    global res 
    if len(s) == k:
        res = min(res,cal(s))
        return 
    
    for i in range(2,n+1):
        if i!=last and (not s or s[-1] < i):
            s.append(i)
            dfs()
            s.pop()

def cal(lst):
    for i in lst:
        f[i] = 0

    de = degree[:]

    tmp = [0]*(n+1)
    queue = deque([(1,0)])
    while True:
        x,t = queue.popleft()

        for nx in d[x]:
            tmp[nx] = max(tmp[nx], t+f[x])

            de[nx] -= 1
            if de[nx] == 0:
                queue.append((nx,tmp[nx]))

        if not queue:
            for i in lst:
                f[i] = time[i]

            return tmp[x] + f[x]
        
def find():
    de = degree[:]
    queue = deque([1])
    while True:
        x = queue.popleft()

        for nx in d[x]:
            de[nx] -= 1
            if de[nx] == 0:
                queue.append(nx)

        if not queue:
            return x

n,m,k = map(int,input().split())
time = [0] + list(map(int,input().split()))
f = time[:]
d = [[] for _ in range(n+1)]

degree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    degree[b] += 1

res = int(1e9)
last = find()
s = []
dfs()
print(res)

