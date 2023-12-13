n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    print(*[i]*n)