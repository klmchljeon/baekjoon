n,k = map(int,input().split())
st = input()
k = min(k,n+1)

p = 'UDLR'
dic = dict(zip(p,range(4)))
dx = (-1,1,0,0)
dy = (0,0,-1,1)

x,y = 0,0
for _ in range(k):
    for i in range(n):
        x += dx[dic[st[i]]]
        y += dy[dic[st[i]]]
        if not (x or y):
            print('YES')
            exit()

print('NO')