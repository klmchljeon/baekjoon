n,k,m = map(int,input().split())
k-=1

alpha = [chr(i+ord('a')) for i in range(26)]
alpha += ['[',']','-']
alpha.sort()

dic = dict(zip(alpha,[dict() for _ in range(len(alpha))]))

for _ in range(n):
    st = input()
    for i in range(len(st)-1):
        if not st[i+1] in dic[st[i]]:
            dic[st[i]][st[i+1]] = 0

        dic[st[i]][st[i+1]] += 1

idx = dict(zip(alpha,range(len(alpha))))
lst = []
for i in alpha:
    tmp = (-1,'')
    for j in dic[i]:
        if tmp[0] < dic[i][j]:
            tmp = (dic[i][j],j)
        elif tmp[0] == dic[i][j] and tmp[1] > j:
            tmp = (dic[i][j],j)

    lst.append(tmp[1])

res = ['[']
a = None
while res[-1] != ']':
    p = lst[idx[res[-1]]]
    if p in res:
        a = res.index(p)
        break

    res.append(p)

ans = []
l = len(res)
for i in range(k,k+m):
    if i < l:
        ans.append(res[i])

    else:
        if a == None:
            ans += ['.']*(k+m-i)
        else:
            cycle = res[a:]
            s = (i-a)%(len(res)-a)
            ans += (cycle*(k+m-i+1))[s:s+k+m-i]
        break

print(''.join(ans))