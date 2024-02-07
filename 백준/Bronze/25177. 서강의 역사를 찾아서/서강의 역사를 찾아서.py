n,m = map(int,input().split())
a = list(map(int,input().split())) 
b = list(map(int,input().split()))

a += [0]*(len(b)-len(a))
b += [0]*(len(a)-len(b))

res = 0
for i in range(len(a)):
    res = max(res,b[i]-a[i])

print(res)