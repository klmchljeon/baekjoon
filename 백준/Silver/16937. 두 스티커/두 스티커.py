def check(a,b):
    if a[0] > h or b[0] > h: return False
    if a[1] > w or b[1] > w: return False

    f1 = (a[0]+b[0]-h)
    f2 = (a[1]+b[1]-w)
    return f1 <= 0 or f2 <= 0

def cal(a,b):
    return a[0]*a[1] + b[0]*b[1]

h,w = map(int,input().split())
n = int(input())
lst = []
for _ in range(n):
    r,c = map(int,input().split())
    lst.append((r,c))

res = 0
for i in range(n-1):
    for j in range(i+1,n):
        for a in (lst[i],lst[i][::-1]):
            for b in (lst[j],lst[j][::-1]):
                if check(a,b):
                    res = max(res,cal(a,b))

print(res)