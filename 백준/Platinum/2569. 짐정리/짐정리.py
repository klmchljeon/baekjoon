#짐정리
def cal(idx,c):
    visit[d[d[idx][1]][1]] = True
    c.append(d[d[idx][1]][1])
    a,b = idx,d[idx][1]
    d[a],d[b] = d[b],d[a]
    
    if idx == d[idx][1]: return c
    else: return cal(idx,c)

n = int(input())
lst = [int(input()) for _ in range(n)]

d = []
for i in range(n):
    d.append((lst[i],i))

d.sort()

cycle = []
visit = [False]*n
for i in range(n):
    if visit[i]: continue

    if d[i][1] != i:
        visit[d[i][1]] = True
        cycle.append(cal(i,[d[i][1]]))
    
    else:
        visit[i] = True

cost = []
for c in cycle:
    tmp = [lst[i] for i in c]
    tmp.sort()
    cost.append(tmp)

minv = min(lst)

res = 0
for i in cost:
    sumi = sum(i)
    a = sumi + len(i)*minv + (i[0] + minv)
    b = sumi-i[0] + (len(i)-1)*i[0]
    
    res += min(a,b)

print(res)