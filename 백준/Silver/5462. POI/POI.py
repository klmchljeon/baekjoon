def cal(d):
    res = 0
    for i in range(t):
        res += score[i]*d[i]

    return res

n,t,p = map(int,input().split())
p -= 1

score = [n]*t
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in range(t):
        score[i] -= tmp[i]

    lst.append(tmp)

k = (cal(lst[p]),sum(lst[p]),-p)
res = 1

for i in range(n):
    a = cal(lst[i])
    b = sum(lst[i])
    c = -i
    if (a,b,c) > k:
        res += 1

print(k[0],res)