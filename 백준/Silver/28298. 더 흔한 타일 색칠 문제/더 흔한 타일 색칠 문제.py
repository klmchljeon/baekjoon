#더 흔한 타일 색칠 문제
max_ = int(1e9)
n,m,k = map(int,input().split())
d = [list(input()) for _ in range(n)]

alpha = [chr(i+ord('A')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

res = [0,['a']*(k**2)]
num = n*m // (k**2)
idx = 0
for x in range(k):
    for y in range(k):

        cnt = [0]*26
        for i in range(x,n,k):
            for j in range(y,m,k):
                cnt[dic[d[i][j]]] += 1

        tmp = [0,None]
        for i in range(26):
            if cnt[i] > tmp[0]:
                tmp = [cnt[i],alpha[i]]

        res[0] += num-tmp[0]
        res[1][idx] = tmp[1]
        idx += 1

ans = [['']*m for _ in range(n)]
for i in range(0,n,k):
    for j in range(0,m,k):

        idx = 0
        for x in range(i,i+k):
            for y in range(j,j+k):
                ans[x][y] = res[1][idx]

                idx += 1

print(res[0])
for i in ans:
    print(*i,sep='')