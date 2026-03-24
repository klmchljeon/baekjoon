alpha = 'ACGT'
dic = dict(zip(alpha,range(4)))

n,m = map(int,input().split())
lst = []
for i in range(n):
    st = input()
    lst.append(st)

res = []
s = 0
for idx in range(m):
    cnt = [0]*4
    for i in range(n):
        cnt[dic[lst[i][idx]]] += 1

    p = -1
    val = 0
    for i in range(4):
        if val < cnt[i]:
            val = cnt[i]
            p = i

    res.append(alpha[p])
    s += n-val

print(''.join(res))
print(s)