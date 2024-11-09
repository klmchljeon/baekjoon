n,k = map(int,input().split())
a = list(map(int,input().split()))
lst = [[a[i],i+1] for i in range(k)]

lst.sort()
max_ = lst[-1][0]
m = n//2 + n%2
if max_ > m:
    print(-1)
    exit()

tmp = []
for i in range(m):
    tmp.append(lst[-1][1])
    lst[-1][0] -= 1
    if lst[-1][0] == 0:
        lst.pop()

lst = lst[::-1]

res = []
odd = 1
for i in range(n):
    if odd:
        res.append(tmp.pop())
    else:
        res.append(lst[-1][1])
        lst[-1][0] -= 1
        if lst[-1][0] == 0:
            lst.pop()

    odd ^= 1

print(*res)