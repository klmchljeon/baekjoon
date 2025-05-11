n = int(input())
lst = [int(input()) for _ in range(n)]
p = 0
for i in range(n):
    if i%2 == 0:
        p += lst[i]
    else:
        p -= lst[i]

res = [p//2]
for i in range(n-1):
    res.append(lst[i]-res[-1])

print(*res,sep='\n')