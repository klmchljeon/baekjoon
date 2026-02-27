n = int(input())
lst = list(map(int,input().split()))
lst.sort()

cur = 0
for i in range(n):
    cur += lst[i] - lst[0]

res = cur
idx = 0
for i in range(1,n):
    dist = lst[i]-lst[i-1]
    cur += i * dist
    cur -= (n-i) * dist

    if res > cur:
        res = cur
        idx = i

print(lst[idx])