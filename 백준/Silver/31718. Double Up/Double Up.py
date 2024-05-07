n = int(input())
d = list(map(int,input().split()))

for i in range(n):
    while d[i]%2 == 0:
        d[i] //= 2

dic = dict()
for i in d:
    if not i in dic:
        dic[i] = 0

    dic[i] += 1

res = 0
for i in dic:
    res = max(res,dic[i])

print(res)