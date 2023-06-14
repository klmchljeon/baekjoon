#올림픽
f = lambda x:(-x[1],-x[2],-x[3])

n,k = map(int,input().split())
d = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    d.append(tmp)

d.sort(key = f)

res = [0]*(n+1)
prev = [None,0]
for i in range(n):
    res[d[i][0]] = prev[1] + (d[i][1:]!=prev[0])

    prev = [d[i][1:],res[d[i][0]]]

print(res[k])