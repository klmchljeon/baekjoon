#숨바꼭질 3

from collections import deque

def bfs(n):
    queue = deque([n])
    visit[n] = 0

    while queue:
        x = queue.popleft()

        vec = [x-1,2*x,x+1]
        for i in range(3):
            if 0<=vec[i]<=100000:
                if visit[vec[i]] == -1:
                    visit[vec[i]] = visit[x] + (i+1)%2
                    queue.append(vec[i])

n,k = map(int,input().split())
visit = [-1]*(100001)
bfs(n)
print(visit[k])  