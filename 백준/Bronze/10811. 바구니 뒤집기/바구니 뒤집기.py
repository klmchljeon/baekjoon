#바구니 뒤집기
n,m = map(int,input().split())
d = [i for i in range(1,n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    d[a:b] = d[a:b][::-1]

print(*d)