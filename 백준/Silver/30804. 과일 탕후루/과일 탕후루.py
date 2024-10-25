n = int(input())
lst = list(map(int,input().split()))
e = 0
dic = dict()
res = 0
for s in range(n):
    while e < n:
        if not lst[e] in dic:
            if len(dic) == 2:
                break
            else:
                dic[lst[e]] = 0

        dic[lst[e]] += 1
        e += 1

    res = max(res,e-s)
    dic[lst[s]] -= 1
    if dic[lst[s]] == 0:
        dic.pop(lst[s])

print(res)