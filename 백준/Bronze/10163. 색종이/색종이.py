n = int(input())
lst = [[n]*1001 for _ in range(1001)]
for i in range(n):
    x,y,w,h = map(int,input().split())
    for nx in range(x,x+w):
        for ny in range(y,y+h):
            lst[nx][ny] = i

res = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        res[lst[i][j]] += 1

print(*res[:-1],sep='\n')