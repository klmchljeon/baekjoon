max_ = int(1e9)

def dist(a,b):
    return abs(a[1]-b[1]) + abs(a[2]-b[2])

n,t = map(int,input().split())
lst = []
for _ in range(n):
    s,x,y = map(int,input().split())
    lst.append((s,x,y))

d = []
for i in range(n):
    tmp = max_
    for j in range(n):
        if lst[j][0] == 1:
            tmp = min(tmp,dist(lst[i],lst[j]))

    d.append(tmp)

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    a-=1;b-=1
    
    t1 = dist(lst[a],lst[b])
    t2 = t + d[a] + d[b]
    print(min(t1,t2))