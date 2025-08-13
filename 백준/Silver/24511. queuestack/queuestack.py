n = int(input())
d = list(map(int,input().split()))
lst = list(map(int,input().split()))
m = int(input())
arr = list(map(int,input().split()))

res = []
for i in range(n)[::-1]:
    if d[i]: continue

    res.append(lst[i])
    m -= 1
    if not m: break

for i in range(m):
    res.append(arr[i])

print(*res)