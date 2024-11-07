def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def cal(a,b,c):
    return area(dist(a,b),dist(a,c),dist(b,c))

n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

res = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            res = max(res,cal(lst[i],lst[j],lst[k]))

print(res)