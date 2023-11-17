def cal(lst):
    res = 1
    for i in range(3):
        for j in range(i+1,4):
            res *= lst[i]+lst[j]

    return res%100

tmp = 'LOVE'
dic = dict(zip(tmp,range(4)))

cnt = [0]*4
st = input()
for i in st:
    if i in dic:
        cnt[dic[i]] += 1

n = int(input())
d = [input() for _ in range(n)]
d.sort()

ans = [None,-1]
for st in d:
    t = cnt[:]
    for i in st:
        if i in dic:
            t[dic[i]] += 1

    num = cal(t)
    if ans[1] < num:
        ans = [st,num]

print(ans[0])