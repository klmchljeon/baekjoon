n = int(input())
d = list(map(int,input().split()))

lst = [[] for _ in range(3)]
for i in d:
    lst[i%3].append(i)

flag1 = (lst[1] and lst[2]) and not lst[0]
flag2 = len(lst[1])+len(lst[2])+1<len(lst[0])

if flag1 or flag2:
    print(-1)
    exit()

res = []
if lst[0]:
    res.append(lst[0].pop())

while lst[1]:
    res.append(lst[1].pop())

    if lst[0]:
        res.append(lst[0].pop())


res = res[::-1]

while lst[2] or lst[0]:
    if lst[2]:
        res.append(lst[2].pop())
    
    if lst[0]:
        res.append(lst[0].pop())

print(*res)