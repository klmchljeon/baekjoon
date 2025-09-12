n = int(input())
lst = list(map(int,input().split()))

p = [(lst[i],i+1) for i in range(n)]
p.sort(reverse=True)

idx = 0
max_ = p[0][0]
tmp = max_
val = tmp
for i in range(n):
    tmp -= max_
    max_ = p[i][0]
    tmp += max_*2

    if val < tmp:
        val = tmp
        idx = i

print(idx+1)
print(*[p[i][1] for i in range(idx+1)])