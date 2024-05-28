n = int(input())
dic = dict()
for _ in range(n):
    p,s = input().split()
    if not s in dic:
        dic[s] = []

    dic[s].append(p)

res = []
for i in dic:
    if i=='-' or len(dic[i])!=2:
        continue

    res.append(dic[i])

print(len(res))
for i in res:
    print(*i)