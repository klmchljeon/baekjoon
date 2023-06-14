#멀티탭 스케줄링
max_ = 1000
m = 100

n,k = map(int,input().split())
d = list(map(int,input().split()))

lst = [max_]*k
prev = [None]*(m+1)
for i in range(k-1,-1,-1):
    if prev[d[i]]:
        lst[i] = prev[d[i]] - i

    prev[d[i]] = i

visit = [-1]*(m+1)
cnt = 0
l = 0
for x,nx in zip(d,lst):
    for i in range(1,m+1):
        if not visit[i] in (-1,max_):
            visit[i] -= 1

    if visit[x] != -1:
        visit[x] = nx
        continue

    if l != n:
        visit[x] = nx
        l += 1
        continue

    tmp = [None,-1]
    for i in range(1,m+1):
        if tmp[1] < visit[i]:
            tmp = [i,visit[i]]

    visit[tmp[0]] = -1
    visit[x] = nx

    cnt += 1

print(cnt)