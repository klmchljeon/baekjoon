def dfs(x,d,cnt=0):
    print('-'*2*cnt + x)
    key = []
    for nx in d[x]:
        key.append(nx)

    key.sort()
    for nx in key:
        dfs(nx,d[x],cnt+1)

dic = dict()

n = int(input())
for _ in range(n):
    k,*lst = input().split()
    k = int(k)

    tmp = dic
    for i in lst:
        if not i in tmp:
            tmp[i] = dict()

        tmp = tmp[i]

key = sorted(dic.keys())
for i in key:
    dfs(i,dic)