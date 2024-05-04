n,m = map(int,input().split())
lst = [[m],[n]]
k = int(input())
for _ in range(k):
    p,x = map(int,input().split())
    lst[p].append(x)

res = []
for i in (0,1):
    lst[i].sort()

    prev = 0
    tmp = 0
    for j in lst[i]:
        tmp = max(tmp,j-prev)
        prev = j

    res.append(tmp)

print(res[0]*res[1])