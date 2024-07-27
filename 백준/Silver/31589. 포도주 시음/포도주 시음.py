n,k = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()
s,e = 0,n-1
res = 0 
cur = 0
while k:
    if lst[e] <= cur:
        cur = lst[s]
        s += 1
        
    else:
        res += lst[e] - cur
        cur = lst[e]
        e -= 1

    k -= 1

print(res)