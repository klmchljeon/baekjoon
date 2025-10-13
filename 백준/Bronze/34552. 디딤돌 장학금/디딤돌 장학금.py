lst = list(map(int,input().split()))
n = int(input())
res = 0
for _ in range(n):
    b,l,s = input().split()
    b,s = map(int,(b,s))
    l = float(l)
    if s >= 17 and l >= 2.0:
        res += lst[b]

print(res)