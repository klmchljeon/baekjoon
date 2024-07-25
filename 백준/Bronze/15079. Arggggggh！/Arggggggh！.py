p = 2**0.5 / 2

lst = ['N','NE','E','SE','S','SW','W','NW']
dic = dict(zip(lst,range(8)))

dx = (0,p,1,p,0,-p,-1,-p)
dy = (1,p,0,-p,-1,-p,0,p)

n = int(input())
x,y = map(int,input().split())
for _ in range(n-1):
    di,d = input().split()
    d = int(d)

    x += d*dx[dic[di]]
    y += d*dy[dic[di]]

print(x,y)