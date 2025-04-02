def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

n = int(input())
lst = []
for _ in range(n):
    x,y = map(float,input().split())
    lst.append((x,y))

t = int(input())
for case in range(t):
    m = int(input())
    
    res = 0
    p = list(map(int,input().split()))
    for i in range(m-1):
        res += dist(lst[p[i]],lst[p[i+1]])**0.5

    print(round(res))