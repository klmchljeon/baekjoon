a,b,n = map(int,input().split())
res = []
for i in range(n+1):
    res.append(a//b)
    a = a%b*10

print(res[n])