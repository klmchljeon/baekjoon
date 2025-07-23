n = int(input())
res = 0
for i in range(n):
    a,b = map(float,input().split())
    res += a*b

print(res)