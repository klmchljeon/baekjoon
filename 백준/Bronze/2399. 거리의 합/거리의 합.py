n = int(input())
d = list(map(int,input().split()))

res = 0
for i in range(n):
    for j in range(n):
        res += abs(d[i]-d[j])

print(res)