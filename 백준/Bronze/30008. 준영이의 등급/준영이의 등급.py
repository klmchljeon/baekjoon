n,k = map(int,input().split())
d = list(map(int,input().split()))

lst = [0,5,12,24,41,61,78,90,97,101]

res = []
for i in d:
    idx = 0
    while i*100//n >= lst[idx]:
        idx += 1

    res.append(idx)

print(*res)