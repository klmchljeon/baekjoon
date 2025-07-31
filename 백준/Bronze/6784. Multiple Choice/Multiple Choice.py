n = int(input())
lst = [input() for _ in range(n)]
ans = [input() for _ in range(n)]

cnt = 0
for i in range(n):
    cnt += lst[i] == ans[i]

print(cnt)