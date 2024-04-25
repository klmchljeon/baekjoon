n,m = map(int,input().split())
t = n//2
l, r = t//2 + t%2, t//2

if n==2:
    cnt = 0
    for i in range(10,100):
        cnt += i%m==0
    
    print(cnt)
    exit()

cnt1 = [0]*m
for i in range(10**(l-1), 10**l):
    tmp1 = str(i)
    k1 = int(tmp1+tmp1[r-1::-1])*10**t
    cnt1[k1%m] += 1

cnt2 = [0]*m
for j in range(10**l):
    tmp2 = str(j)
    k2 = '0'*(l-len(tmp2)) + tmp2
    k2 = int(k2+k2[r-1::-1])
    cnt2[k2%m] += 1

res = 0
for i in range(m):
    res += cnt1[i]*(cnt2[(m-i)%m])

print(res)