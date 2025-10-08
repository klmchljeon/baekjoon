def bt():
    if len(s) == d:
        flag = True
        for i in range(d):
            flag &= not visited[i][s[i]]

        if not flag:
            return

        for i in range(d):
            visited[i][s[i]] = True

        res.append(tuple(s))
        return
    
    for i in range(d):
        if not i in s:
            s.append(i)
            bt()
            s.pop()

    return

n,d = map(int,input().split())

s = []
res = []
visited = [[False]*d for _ in range(d)]

bt()

ans = [[0]*n for _ in range(n)]
for i in range(n-d):
    for j in range(n-d,n):
        ans[i][j] = j-(n-d)

for j in range(n-d):
    for i in range(n-d,n):
        ans[i][j] = i-(n-d)

for i in range(n-d,n):
    for j in range(n-d,n):
        ans[i][j] = res[i-(n-d)][j-(n-d)]

for i in ans:
    print(*i)