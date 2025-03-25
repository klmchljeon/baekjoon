def bt(cur,cnt):
    res[cur%2] = max(res[cur%2],cnt)
    if cur >= 2*n:
        return 

    flag = True
    for k in range(*p[cur]):
        if lst[k+idx[cur]][k] and tmp[k+idx[cur] + k]:
            flag = False
            tmp[k+idx[cur] + k] = False
            bt(cur+2,cnt+1)
            tmp[k+idx[cur] + k] = True

    if flag:
        bt(cur+2,cnt)

n = int(input())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

tmp = [True]*(2*n+1)
idx = list(range(n-1,-n,-1))
p = [(0,i+1) for i in range(n)] + [(i+1,n) for i in range(n)]

res = [0,0]

bt(0,0)
bt(1,0)

print(sum(res))