n = int(input())
d = list(map(int,input().split()))

p = []
m = []

def findp(num):
    if len(p)==0:
        return 0
    
    s,e = -1,len(p)
    while s+1<e:
        mid = (s+e)//2

        if p[mid] <= num:
            s = mid
        else:
            e = mid

    return len(p) - (s+1)
    
def findm(num):
    if len(m)==0:
        return 0
    
    num = -num
    s,e = -1,len(m)
    while s+1<e:
        mid = (s+e)//2

        if m[mid] <= num:
            s = mid
        else:
            e = mid

    return len(m) - (s+1)

for i in d:
    if i <= 0:
        m.append(i)
    else:
        p.append(i)

m.sort()
p.sort()

res = []
for i in range(n+1):
    if findm(i) + findp(i) == i:
        res.append(i)

print(len(res))
print(*res)