mod = int(1e9)+7

n,m = map(int,input().split())
lst = list(map(int,input()))

mod10 = []
tmp = 1
for i in range(n):
    mod10.append(tmp)
    tmp = (tmp*10)%m

q = []
tmp = 0
for i in range(n):
    tmp = (tmp+lst[n-i-1]*mod10[i])%m
    q.append(tmp)

q = q[::-1]

cnt = 0
p = 0
for i in range(n):
    cnt += p+q[i]==0

    p = (p*10 + lst[i])%m

if cnt == 0:
    print(0)
else:
    res = 1
    for i in range(cnt-1):
        res = (res*2)%mod

    print(res)
