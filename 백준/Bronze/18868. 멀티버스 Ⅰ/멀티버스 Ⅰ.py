def check(a,b):
    fir = cur(a[0],b[0])
    for i in range(1,n):
        if fir != cur(a[i],b[i]):
            return False
        
    return True

def cur(p,q):
    if p > q:
        return 0
    
    if p == q:
        return 1
    
    return 2

m,n = map(int,input().split())
lst = []
for _ in range(m):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

d = []
for c in lst:
    arr = []
    for i in range(n-1):
        for j in range(1,n):
            arr.append(cur(c[i],c[j]))

    d.append(arr)

cnt = 0
for i in range(m-1):
    for j in range(i+1,m):
        cnt += d[i]==d[j]

print(cnt)