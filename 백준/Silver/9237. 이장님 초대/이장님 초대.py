n = int(input())
d = list(map(int,input().split()))

d.sort(reverse=1)

res = 0
for i in range(n):
    res = max(res, d[i]+i+2)

print(res)