n = int(input())
lst = list(map(int,input().split()))
u,d = map(int,input().split())

cnt = [0]*4
for i in lst:
    cnt[i] += 1

f1 = cnt[1]+cnt[3] < u
f2 = cnt[2]+cnt[3] < d

if f1 or f2:
    print('NO')
    exit()

res = []
c = cnt[3] + cnt[1] - u
for i in range(n):
    if lst[i] == 1:
        res.append('U')
        u -= 1
    elif lst[i] == 2:
        res.append('D')
        d -= 1
    else:
        res.append('D' if c>0 else 'U')
        c -= 1

print('YES')
print(*res,sep='')