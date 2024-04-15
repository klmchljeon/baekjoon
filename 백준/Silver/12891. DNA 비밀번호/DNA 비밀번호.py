def check(lst):
    for i in range(4):
        if lst[i] < d[i]:
            return 0
        
    return 1

s,p = map(int,input().split())
st = input()
d = list(map(int,input().split()))

alpha = 'ACGT'
dic = dict(zip(alpha,range(4)))

cnt = [0]*4
for i in range(p):
    cnt[dic[st[i]]] += 1

res = check(cnt)
for i in range(p,s):
    cnt[dic[st[i-p]]] -= 1
    cnt[dic[st[i]]] += 1
    res += check(cnt)

print(res)