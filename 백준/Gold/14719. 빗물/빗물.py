#빗물
h,w = map(int,input().split())
d = list(map(int,input().split()))

res = 0
for i in range(1,w-1):
    a = max(d[:i])
    b = max(d[i+1:])
    
    tmp = min(a,b)
    if d[i] > tmp: continue

    res += tmp - d[i]

print(res)