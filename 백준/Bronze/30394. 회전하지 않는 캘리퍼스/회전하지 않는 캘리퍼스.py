n = int(input())
res = [10**9, -10**9]
for _ in range(n):
    _,y = map(int,input().split())
    res[0] = min(res[0],y)
    res[1] = max(res[1],y)
    
print(res[1]-res[0])