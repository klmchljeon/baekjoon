def f(x):
    a,b = x[0],x[1:]
    return dic[a]*(10**4) - int(b)

st = 'BSGPD'
dic = dict(zip(st,range(5)))

n = int(input())
lst = list(input().split())

lst2 = lst[:]
lst2.sort(key = f)

res = []
for i in range(n):
    if lst[i] != lst2[i]:
        res.append(lst2[i])

if not res:
    print('OK')
else:
    print('KO')
    print(*res)