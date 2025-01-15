from collections import defaultdict

n = int(input())
lst = list(map(int,input().split()))

res = 0
for s in range(n-1):
    e = s+1
    dic = defaultdict(int)
    cnt = 0
    while 0<=s and e<n:
        dic[lst[s]] += 1
        if dic[lst[s]] == 1:
            cnt += 1
        if dic[lst[s]] == 0:
            cnt -= 1

        dic[lst[e]] -= 1
        if dic[lst[e]] == -1:
            cnt += 1
        if dic[lst[e]] == 0:
            cnt -= 1

        if cnt == 0:
            res = max(res,e-s+1)

        s -= 1
        e += 1

print(res)