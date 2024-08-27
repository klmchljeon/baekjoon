mod = int(1e9+7)

n = int(input())
lst = list(map(int,input().split()))
res = 0
p = 0
for i in lst:
    p = (p*i + i)%mod
    res = (res + p)%mod

print(res)