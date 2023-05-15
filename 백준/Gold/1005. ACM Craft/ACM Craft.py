#ACM Craft

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n,k = map(int,input().split())
    cost = [0]+list(map(int,input().split()))
    d = [[] for _ in range(n+1)]
    degree = [0]*(n+1)


    for _ in range(k):
        a,b = map(int,input().split())
        d[a].append(b)
        degree[b] += 1
    w = int(input())


    queue = deque()
    dp = [0]*(n+1)
    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)
            dp[i] += cost[i]
            

    while queue:
        x = queue.popleft()

        for i in d[x]:
            degree[i] -= 1
            dp[i] = max(dp[i], dp[x]+cost[i])
            if degree[i] == 0:
                queue.append(i)

    print(dp[w])