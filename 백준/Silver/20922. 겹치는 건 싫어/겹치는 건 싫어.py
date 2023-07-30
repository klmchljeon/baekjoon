n,k = map(int,input().split())
d = list(map(int,input().split()))

lst = [0]*100001

e = 0
res = 0
for s in range(n):
    while e<n and lst[d[e]]<k:
        lst[d[e]] += 1
        e += 1

    res = max(res,e-s)
    lst[d[s]] -= 1

print(res)