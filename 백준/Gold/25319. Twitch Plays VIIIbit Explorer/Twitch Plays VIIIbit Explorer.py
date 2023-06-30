def conv(a,b):
    tmp = []
    if a[0]-b[0] >= 0:
        tmp.append('U'*(a[0]-b[0]))
    else:
        tmp.append('D'*(b[0]-a[0]))

    if a[1]-b[1] >= 0:
        tmp.append('L'*(a[1]-b[1]))
    else:
        tmp.append('R'*(b[1]-a[1]))

    tmp.append('P')

    return ''.join(tmp)

max_ = int(1e9)

n,m,l = map(int,input().split())
d = [list(input()) for _ in range(n)]

st = input()

t = set(st)
lent = len(t)

lst = [[] for _ in range(lent)]

dic = dict(zip(t,range(lent)))

for i in range(n):
    for j in range(m):
        if d[i][j] in dic:
            lst[dic[d[i][j]]].append((i,j))

cnt = [0]*lent
for i in st:
    cnt[dic[i]] += 1

c = max_
for i in range(lent):
    c = min(c,len(lst[i])//cnt[i])

res = []
idx = [0]*lent
cur = (0,0)
for _ in range(c):
    for k in st:
        i = dic[k]
        nxt = lst[i][idx[i]]

        res.append(conv(cur,nxt))
        
        cur = nxt
        idx[i] += 1

res.append(conv(cur,(n-1,m-1))[:-1])

ans = ''.join(res)
print(c,len(ans))
print(ans)