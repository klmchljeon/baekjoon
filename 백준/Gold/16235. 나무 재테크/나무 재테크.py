#나무 재테크 55:10
import sys
input = sys.stdin.readline

def ss():
    lst = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            tmp = []

            while d[x][y]:
                tree = d[x][y].pop()
                if gr[x][y] >= tree:
                    gr[x][y] -= tree

                    tmp.append(tree+1)
                    if (tree+1)%5==0:
                        lst[x][y] += 1

                else:
                    gr[x][y] += tree//2
                    break

            for t in d[x][y]:
                gr[x][y] += t//2

            d[x][y] = tmp[::-1]

    return lst

def fw(lst):
    for x in range(n):
        for y in range(n):
            gr[x][y] += a[x][y]

            if not lst[x][y]: continue

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0<=nx<n and 0<=ny<n):
                    continue

                for _ in range(lst[x][y]):
                    d[nx][ny].append(1)

    return 

dx = (-1,1,0,0,-1,-1,1,1)
dy = (0,0,-1,1,-1,1,-1,1)

n,m,k = map(int,input().split())
a = tuple(tuple(map(int,input().split())) for _ in range(n))

gr = [[5]*(n) for _ in range(n)]
d = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    d[x-1][y-1].append(z)

for _ in range(k):
    fw(ss())

res = 0
for i in range(n):
    for j in range(n):
        res += len(d[i][j])

print(res)