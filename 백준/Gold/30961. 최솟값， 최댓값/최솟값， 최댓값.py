n = int(input())
a = list(map(int,input().split()))

a.sort()
res = a[0]**2
for i in range(1,n):
    res ^= a[i]**2
    res ^= a[i]*a[i-1]

print(res)