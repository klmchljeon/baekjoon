n = int(input())
h = list(map(int,input().split()))
a = list(map(int,input().split()))

a.sort()
res = 0
for i in range(n):
    res += h[i] + a[i]*i

print(res)