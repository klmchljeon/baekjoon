n,m = map(int,input().split())
p = n if m%2==1 else 0

cnt = [0]*(int(1e4) + 1)
for _ in range(n):
    lst = list(map(int,input().split()))
    for i in lst:
        cnt[i] ^= 1

print('YES' if sum(cnt)<=p else 'NO')