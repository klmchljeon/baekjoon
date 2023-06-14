#바구니 순서 바꾸기
n,m = map(int,input().split())
d = list(range(n+1))

for _ in range(m):
    i,j,k = map(int,input().split())
    d[i:j+1] = d[k:j+1] + d[i:k]

print(*d[1:])