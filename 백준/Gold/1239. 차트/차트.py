def bt():
    if len(s) == n:
        tmp.append(tuple(s))
        return

    for i in range(n):
        if not i in s:
            s.append(i)
            bt()
            s.pop()

n = int(input())
lst = list(map(int,input().split()))

s = []
tmp = []
bt()

res = 0
for idx in tmp:
    p = [lst[i] for i in idx]
    
    line = []
    cur = 0
    for i in p:
        line.append(cur)
        cur += i 

    cnt = 0
    for i in line:
        if i >= 50: break
        cnt += (i+50) in line

    res = max(res,cnt)

print(res)