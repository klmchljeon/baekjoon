k = int(input())
lst = list(map(int,input().split()))

res = [[] for _ in range(k)]
for i in range(len(lst)):
    n = i+1
    for j in range(k):
        if n&(1<<j):
            idx = (k-1)-j
            res[idx].append(lst[i])
            break

for i in res:
    print(*i)