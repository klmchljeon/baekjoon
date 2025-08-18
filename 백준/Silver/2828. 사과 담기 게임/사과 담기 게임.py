n,m = map(int,input().split())
k = int(input())
s,e = 1,m
res = 0
for i in range(k):
    a = int(input())
    if a < s:
        dist = s-a
        res += dist
        s -= dist
        e -= dist

    elif e < a:
        dist = a-e
        res += dist
        s += dist
        e += dist

print(res)