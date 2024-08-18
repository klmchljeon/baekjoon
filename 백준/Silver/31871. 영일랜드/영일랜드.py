def gen():
    if len(s) == n:
        lst.append(tuple([0]+s+[0]))
        return 
    
    for i in range(1,n+1):
        if not i in s:
            s.append(i)
            gen()
            s.pop()

    return 

n = int(input())
m = int(input())
graph = [[-1]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,d = map(int,input().split())
    graph[u][v] = max(graph[u][v],d)

lst = []
s = []
gen()

res = -1
for p in lst:
    t = 0
    for i in range(n+1):
        tmp = graph[p[i]][p[i+1]]
        if tmp == -1:
            break

        t += tmp

    else:
        res = max(res,t)

print(res)