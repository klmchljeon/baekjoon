n = int(input())
val = list(map(int,input().split()))
cost = list(map(int,input().split()))

max_ = [[-1,-1],[-1,-1]]
for i in range(n):
    if max_[0][0] < val[i]:
        max_[1] = max_[0][:]
        max_[0] = [val[i],i]

    elif max_[1][0] < val[i]:
        max_[1] = [val[i],i]

tmp = [0]*n
for i in range(n):
    if max_[0][1] != i:
        tmp[i] = max_[0][0] - cost[i]

    else:
        tmp[i] = max_[1][0] - cost[i]

res = [0]*n
for i in range(n):
    res[i] = val[i] - (tmp[i]+cost[i])

print(*res)