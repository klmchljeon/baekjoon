#공 넣기
n,m = map(int,input().split())

lst = [0]*(n+1)
for _ in range(m):
    i,j,k = map(int,input().split())
    lst[i:j+1] = [k]*(j-i+1)

print(*lst[1:])