n = int(input())
lst = list(map(int,input().split()))
res = [0,0]
cur = []
for i in range(n):
    if not cur or cur[-1] <= lst[i]:
        cur.append(lst[i])

    else:
        res[0] += 1
        res[1] = max(res[1],len(cur))
        cur = [lst[i]]

if cur:
    res[0] += 1
    res[1] = max(res[1],len(cur))

print(*res)