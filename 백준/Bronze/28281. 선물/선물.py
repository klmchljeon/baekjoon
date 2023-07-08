n,x = map(int,input().split())
d = list(map(int,input().split()))
tmp = int(1e9)
for i in range(n-1):
    tmp = min(tmp,d[i]+d[i+1])
    
print(tmp*x)