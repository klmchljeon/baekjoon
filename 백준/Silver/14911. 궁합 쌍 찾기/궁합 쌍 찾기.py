lst = list(map(int,input().split()))
m = int(input())
res = []
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == m:
            res.append((lst[i],lst[j]))

ans = sorted(set(res))
for i in ans:
    print(*i)

print(len(ans))