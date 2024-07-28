import datetime

def conv(t):
    tmp = [60,60,24]
    res = t
    for i in tmp:
        res /= i

    return res

n = int(input())
lst = []
for _ in range(n):
    t1,t2,l = input().split()
    l = int(l)
    dt = datetime.datetime(*map(int,t1.split('/')),*map(int,t2.split(':')))
    lst.append((dt,l))

time = []
for dt,_ in lst:
    time.append(conv((lst[n-1][0]-dt).total_seconds()))

p = []
for i in range(n):
    v1 = 0.5**(time[i]/365)
    v2 = 0.9**(n-(i+1))
    p.append(max(v1,v2))

u,d = 0,0
for i in range(n):
    u += p[i]*lst[i][1]
    d += p[i]

if not d:
    print(0)
else:
    print(round(u/d))