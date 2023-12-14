import sys
sys.setrecursionlimit(int(2e5))
input = sys.stdin.readline

def dfs(x):
    lst = [[],[]]
    
    cnt = 0

    for nx in d[x]:
        if visit[nx]: continue

        visit[nx] = True
        tmp = dfs(nx)
        cnt += 1
        lst[tmp[1]].append(tmp[0])

    if cnt == 0:
        return (a[x],1)
    
    if cnt == 1:
        return (a[x]-tmp[0],tmp[1]^1)

    for i in (0,1):
        lst[i].sort()

    t = 0
    while lst[0] and lst[0][-1] >= 0:
        t += lst[0].pop()

    p = 0
    while lst[1]:
        if p:
            t -= lst[1].pop()
        else:
            t += lst[1].pop()
        
        p ^= 1

    if p:
        t -= sum(lst[0])
    else:
        t += sum(lst[0])

    return (a[x]-t,p^1)

n = int(input())
d = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)

a = [0] + list(map(int,input().split()))

visit = [False]*(n+1)
visit[1] = True

res = dfs(1)[0]
if res > 0:
    print('Sehun')
elif res < 0:
    print('Cheolmin')
else:
    print('Draw')