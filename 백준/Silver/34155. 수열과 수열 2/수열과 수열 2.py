mod = 998244353

n = int(input())
lst = list(map(int,input().split()))
res = 1
for i in range(n):
    if i+1 == lst[i]:
        res = (res*(n-1))%mod
    else:
        res = (res*(n-2))%mod
        
print(res)