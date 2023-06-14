#결혼식
n = int(input())
m = int(input())

d = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

q = []

visit = [0]*(n+1)
for i in d[1]:
    visit[i] = 1
    q.append(i)

for x in q:
    for nx in d[x]:
        visit[nx] = 1

print(sum(visit) - bool(q))