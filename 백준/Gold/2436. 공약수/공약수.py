def bt():
    if len(s) == n:
        tmp.append(tuple(s))
        return 
    
    for i in (0,1):
        s.append(i)
        bt()
        s.pop()

g,l = map(int,input().split())
l //= g

dic = dict()
p = 2
while l > 1:
    if l%p == 0:
        if not p in dic:
            dic[p] = 0

        dic[p] += 1
        l //= p

    else:
        p += 1

lst = list(dic.items())
n = len(lst)

s = []
tmp = []
bt()

val = int(1e10)
res = None
for idx in tmp:
    a,b = g,g
    for i in range(n):
        if idx[i]:
            a *= lst[i][0]**lst[i][1]

        else:
            b *= lst[i][0]**lst[i][1]

    if val > a+b:
        val = a+b
        res = (a,b)

print(*sorted(res))