n,m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
input()
cnt = 0
for i in range(n):
    st = list(input())
    for j in range(m):
        cnt += lst[i][j]==st[j]

print(cnt)