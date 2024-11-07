def bt():
    if len(s) == 8:
        idx.append(tuple(s))
        return 
    
    for i in range(8):
        if not i in s:
            s.append(i)
            bt()
            s.pop()

lst = list(map(int,input().split()))
s = []
idx = []
bt()

cnt = 0
for p in idx:
    tmp = [lst[j] for j in p]
    for i in range(8):
        a = tmp[(i-1)%8]
        b = tmp[(i+1)%8]
        x = tmp[i]
        if not ((a+b)*x)**2 > 2*(a*b)**2:
            break

    else:
        cnt += 1

print(cnt)