k,n = map(int,input().split())
k_ = k
p = 2
lst = []
cnt = 0
while k >= p:
    if k%p == 0:
        k //= p
        cnt += p==2
        if not lst or lst[-1] != p:
            lst.append(p)

    else:
        p += 1

res = 0
for num in range(1,n+1):
    cnt2 = 0
    flag = True
    for p in lst:
        if num%p == 0:
            if p == 2:
                tmp = num
                while tmp%p == 0:
                    tmp //= p
                    cnt2 += 1

            else:
                flag = False
                break

    if not flag: continue
    
    if cnt2 == 0 or min(cnt2,cnt) == 1:
        res += 1

print(res if k_ > 2 else res-1)