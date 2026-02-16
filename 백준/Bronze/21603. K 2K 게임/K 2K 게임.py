n,k = map(int,input().split())
lst = [k%10, 2*k%10]

res = []
for i in range(1,n+1):
    if i%10 in lst: continue

    res.append(i)

print(len(res))
print(*res)