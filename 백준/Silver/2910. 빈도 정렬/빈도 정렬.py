n,c = map(int,input().split())
lst = list(map(int,input().split()))
dic = dict()
for i in range(n):
    if not lst[i] in dic:
        dic[lst[i]] = [i,0]

    dic[lst[i]][1] += 1

p = sorted(dic.items(), key = lambda x:(-x[1][1],x[1][0]))
res = []
for i,c in p:
    res.extend([i]*c[1])

print(*res)