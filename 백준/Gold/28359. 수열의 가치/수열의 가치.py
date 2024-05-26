n = int(input())
d = list(map(int,input().split()))
d.sort()

res = sum(d)
prev = None
tmp = 0
s = 0
for i in range(n-1,-1,-1):
    if prev == d[i]:
        tmp += d[i]

    else:
        s = max(s,tmp)
        tmp = d[i]

    prev = d[i]

s = max(s,tmp)

print(res + s)
print(*d)