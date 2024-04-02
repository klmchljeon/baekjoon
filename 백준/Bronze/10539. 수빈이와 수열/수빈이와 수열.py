n = int(input())
d = list(map(int,input().split()))
res = []
s = 0
for i in range(n):
    tmp = d[i]*(i+1) - s
    s += tmp
    res.append(tmp)

print(*res)