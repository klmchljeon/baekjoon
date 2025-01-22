n,m = map(int,input().split())
lst = list(map(int,input().split())) + [0]*m
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n+m):
        lst[i] -= tmp[j]
        lst[j] += tmp[j]

print(*lst)