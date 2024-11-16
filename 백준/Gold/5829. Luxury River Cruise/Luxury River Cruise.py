n,m,k = map(int,input().split())
graph = [()]
for i in range(n):
    l,r = map(int,input().split())
    graph.append((l,r))

lst = [i=='R' for i in input().split()]

p = [0]
for s in range(1,n+1):
    for i in lst:
        s = graph[s][i]

    p.append(s)

cnt = 0
s = 1
while cnt < k:
    s = p[s]
    cnt += 1
    if s == 1:
        break

else:
    print(s)
    exit()

k %= cnt
cnt = 0
while cnt < k:
    s = p[s]
    cnt += 1

print(s)